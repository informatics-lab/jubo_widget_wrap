from bokeh.models.widgets.sliders import Slider as BokehSlider
from bokeh.models.widgets import Select as BokehSelect


class JuboWidgetMixIn():
    """Mixin to identity this class as a Jubo Widget"""
    pass


class JuboDropdown(BokehSelect, JuboWidgetMixIn):
    __view_model__ = "JuboDropdown"
    __implementation__ = """
    import {Select} from "models/widgets/selectbox"
    export class JuboDropdown extends Select
        type: "JuboDropdown"
    """

    def __init__(self, **kwargs):
        if "description" in kwargs:
            kwargs["title"] = kwargs["description"]
            del kwargs["description"]

        return super().__init__(**kwargs)

    def add_interact(self, callback):
        self.on_change('value', lambda __1, __2, __3: callback())


class JuboIntSlider(BokehSlider, JuboWidgetMixIn):
    __view_model__ = "JuboIntSlider"
    __implementation__ = """
    import {Slider} from "models/widgets/slider"
    export class JuboIntSlider extends Slider
        type: "JuboIntSlider"
    """

    def __init__(self, value=None, min=None, max=None, step=None, **kwargs):
        if "description" in kwargs:
            kwargs["title"] = kwargs["description"]
            del kwargs["description"]

        return super().__init__(start=min, end=max, value=value, step=step, **kwargs)

    def add_interact(self, callback):
        self.on_change('value', lambda __1, __2, __3: callback())
