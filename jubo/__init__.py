
try:  # Better test?
    get_ipython()
    IS_BOKEH = False
except NameError:
    IS_BOKEH = True


if IS_BOKEH:
    from .bokeh_wrappers import interact, append, cell, current_output_element, display_patched
else:
    # Assume note book
    from ipywidgets import interact
