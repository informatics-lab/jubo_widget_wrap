from jubo import IS_BOKEH

if IS_BOKEH:
    from .bokeh_wrappers import JuboIntSlider as IntSlider, JuboDropdown as Dropdown
else:
    from ipywidgets import IntSlider, Dropdown
