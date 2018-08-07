
try:  # Better test?
    get_ipython()
    IS_BOKEH = False
except NameError:
    IS_BOKEH = True


if IS_BOKEH:
    from .bokeh_wrappers import interact, append
else:
    # Assume note book
    from ipywidgets import interact
