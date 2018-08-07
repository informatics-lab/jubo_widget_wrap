from .widgets import *
from bokeh.layouts import column
from bokeh.io import curdoc
from bokeh.models import Model
from bokeh.models.widgets import Div
from bokeh.models.widgets import PreText


doc_root = column()
curdoc().add_root(doc_root)


def append(widgets):
    doc_root.children.append(column(widgets))


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

    def callback():
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

    doc_root.children.append(dom_widgets + [output_widget])
