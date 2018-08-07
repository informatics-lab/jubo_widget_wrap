# JUBO Widget Wrapper

An experiment in bridging the gap between Jupyter Notebooks using `ipywidgets` and a Bokeh server application. 
The idea is to test if this might be a good way of sharing prototype apps built in the notebook.

In this experiment the `jubo` module implements methods/classes from `ipywidgets`. If used in a notebook context
these will simply be the `ipywidgets` objects, in a Bokeh context they will be Bokeh objects wrapped to implement (a very limited set of) the
`ipywidgets` interface.

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

View and run `simple-interactive.ipynb`

convert to python

`jupyter nbconvert --to python notebooks/simple-interactive.ipynb --output-dir=bokeh_apps