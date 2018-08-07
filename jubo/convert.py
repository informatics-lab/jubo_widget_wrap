from nbconvert import PythonExporter
from sys import argv
import os
import shutil
from jinja2 import DictLoader

tmplt = """{%- extends 'null.tpl' -%}

{%- block header -%}
#!/usr/bin/env python
# coding: utf-8

import jubo
{% endblock header %}

{% block in_prompt %}
{% if resources.global_content_filter.include_input_prompt -%}
# In[{{ cell.execution_count if cell.execution_count else ' ' }}]:
{% endif %}
{% endblock in_prompt %}

{% block input %}
with jubo.cell("cell_{{ range(1000) | random }}{{ range(1000) | random }}{{ range(1000) | random }}"):
    with jubo.display_patched():
{{ cell.source | ipython2python | indent | indent}}
{% endblock input %}

{% block markdowncell scoped %}
{{ cell.source | comment_lines }}
{% endblock markdowncell %}"""

dl = DictLoader({'python.tpl': tmplt})
pyex = PythonExporter(extra_loaders=[dl])


def convert(infile, outfile):
    (code, _) = pyex.from_filename(infile)

    with open(outfile, 'w') as ofp:
        ofp.write(code)


if __name__ == "__main__":
    innb = os.path.abspath(os.path.join('.', argv[1]))
    outpy = os.path.abspath(os.path.join('.', argv[2]))

    convert(innb, outpy)
