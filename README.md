# JUBO Widget Wrapper

An experiment in bridging the gap between Jupyter Notebooks using `ipywidgets` and a Bokeh server application. 
The idea is to test if this might be a good way of sharing prototype apps built in the notebook.

In this experiment the `jubo` module implements methods/classes from `ipywidgets`. If used in a notebook context
these will simply be the `ipywidgets` objects, in a Bokeh context they will be Bokeh objects wrapped to implement (a very limited set of) the
`ipywidgets` interface. Additionally there is some patching of `IPython` to capture output to be displayed and render it in Bokeh.

## Requirements

* jupyter-lab
* ipywidgets
* bokeh

A verbose `requirements.txt` file is also included in the repo.

## Demo

Enable the `ipywidgets` Lab extension:

`jupyter labextension install @jupyter-widgets/jupyterlab-manager`

Start Jupyter Lab with `jubo` on the `PYTHONPATH`:

`PYTHONPATH=../:$PYHTONPATH jupyter lab --notebook-dir=notebooks`

View and run `simple-interactive.ipynb` or `images.ipynb`

convert to python

`jubo/convert.py notebooks/images.ipynb bokeh_apps/images.py` or 
`jubo/convert.py  notebooks/simple-interactive.ipynb bokeh_apps/simple-interactive.py`

serve

`bokeh serve bokeh_apps/simple-interactive.py --show` or
`bokeh serve bokeh_apps/images.py --show`