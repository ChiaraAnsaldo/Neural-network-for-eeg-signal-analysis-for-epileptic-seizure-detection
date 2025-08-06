# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'TNE_HM_model'
copyright = '2025, Claudio Verardo'
author = 'Claudio Verardo'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon', 'sphinxcontrib.matlab', 'sphinx_autodoc_typehints', 'sphinx.ext.intersphinx',]


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

napoleon_google_docstring = True
napoleon_numpy_docstring = True
nitpicky = False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']
html_js_files = ['custom.js']

matlab_src_dir = 'C:/Users/Lenovo/Desktop/Chiara/Tesi/TNE_HM_nerves'
matlab_short_links = True
matlab_keep_package_prefix = False
matlab_auto_link = 'basic'

sys.path.insert(0, os.path.abspath('../../..'))

sys.path.insert(0, os.path.abspath('./_ext'))

def process_docstring(app, what, name, obj, options, lines):
    formatted_lines = []
    inside_section = False
    buffer = []

    for i, line in enumerate(lines):
        if "NAME, VALUE ARGS:" in line:
            formatted_lines.append("")
            formatted_lines.append(".. admonition:: NAME, VALUE ARGS:")
            formatted_lines.append("   :class: name-value-args")
            formatted_lines.append("")

            inside_section = True
            continue  

        if line.startswith("EXPORT FILE"):
            formatted_lines.append("")
            formatted_lines.append(".. admonition:: "+ line.strip())
            formatted_lines.append("   :class: export-file")
            formatted_lines.append(" ")  
            inside_section = True
            continue  

        if inside_section:
            if line.strip() == "":
                inside_section = False
                formatted_lines.extend(["   " + l for l in buffer])
                formatted_lines.append("") 
                buffer = []
                formatted_lines.append("")  
                formatted_lines.append(line)
            else:
                buffer.append(line)
        else:
            formatted_lines.append(line)

    if inside_section:
        formatted_lines.extend(["   " + l for l in buffer])
        formatted_lines.append("")

    lines[:] = formatted_lines


def setup(app):
    app.connect("autodoc-process-docstring", process_docstring)
