from .widgets import *
from bokeh.layouts import column
from bokeh.io import curdoc
from bokeh.models import Model
from bokeh.models.widgets import Div
from bokeh.models.widgets import PreText
from contextlib import contextmanager
from unittest.mock import patch
import IPython.core.interactiveshell

doc_root = column()
curdoc().add_root(doc_root)


def append(widget):
    doc_root.children.append(widget)


def dom_widget_for_thing(thing):
    if isinstance(thing, Model):
        print("is model")
        dom_widget = thing
    elif hasattr(thing, '__html__'):
        print("is html")
        dom_widget = Div(text=thing.__html__())
    else:
        print("is text")
        dom_widget = PreText(text=str(thing))

    return dom_widget


def interact(method, **kwargs):
    print(kwargs)

    output_area = current_output_element()

    def callback():
        with display_patched(output_area):
            clear_output()
            method_kwards = {k: getattr(v, 'value', v) for k, v in kwargs.items()}
            return method(**method_kwards)

    output_widget = dom_widget_for_thing(callback())

    def updating_callback():
        result = callback()
        output_widget.text = str(result)

    dom_widgets = []
    for widget in kwargs.values():
        if isinstance(widget, JuboWidgetMixIn):
            if hasattr(widget, 'add_interact'):
                widget.add_interact(updating_callback)
            dom_widgets.append(dom_widget_for_thing(widget))

    current_cell_container().children.append(column(dom_widgets + [output_widget]))


cell_containers = {}
cell_stack = []


def current_cell_container():
    return cell_stack[-1]


def current_output_element():
    return current_cell_container().children[0]


@contextmanager
def cell(cell_id):
    if not cell_id in cell_containers:
        container = column([Div(text="")])
        append(container)
        cell_containers[cell_id] = container
    cell_stack.append(cell_containers[cell_id])
    try:
        yield
    finally:
        cell_stack.pop(-1)


ishell = IPython.core.interactiveshell.InteractiveShell.instance()


output_area_stack = []


def clear_output():
    output_area = output_area_stack[-1]
    output_area.children = []


def publish(data, **kwargs):
    output_area = output_area_stack[-1]
    print("display")
    if 'text/html' in data:
        output_area.children.append(Div(text=data['text/html']))
    elif 'text/plain' in data:
        output_area.children.append(Div(text=data['text/plain']))


@contextmanager
def display_patched(output_area=None):
    if output_area is None:
        output_area = current_output_element()
    output_area_stack.append(output_area)
    with patch("IPython.core.displaypub.DisplayPublisher.publish", wraps=publish) as mock_publish:
        yield
    output_area_stack.pop()
