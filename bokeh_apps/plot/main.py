import jubo
from unittest.mock import patch
import IPython.core.interactiveshell
from bokeh.models.widgets import Div
import sys
import os

sys.path = [os.path.dirname(__file__)] + sys.path
ishell = IPython.core.interactiveshell.InteractiveShell.instance()

content = Div(text="...")
jubo.append(content)


def publish(data, **kwargs):
    if 'text/html' in data:
        content.text = data['text/html']
    elif 'text/plain' in data:
        content.text = data['text/plain']


with patch("IPython.core.displaypub.DisplayPublisher.publish", wraps=publish) as mock_publish:
    import notebook
