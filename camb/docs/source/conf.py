# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath('../..'))
print(os.path.abspath('../..'))
print("...............................................")

# -- Project information -----------------------------------------------------

project = 'isitgr'
copyright = '2020, Cristhian Garcia-Quintero, Mustapha Ishak, Jason Dossett'
author = 'Cristhian Garcia-Quintero, Mustapha Ishak, Jason Dossett'

# The full version, including alpha/beta/rc tags
release = '1.0.2'


# -- General configuration ---------------------------------------------------


nitpicky = True

# Prevent spurious errors for every field ivar (not sure why..)
def on_missing_reference(app, env, node, contnode):
    if node['reftype'] == 'obj':
        return contnode
    else:
        return None


def setup(app):
    app.connect('missing-reference', on_missing_reference)


# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.3'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc', 'sphinx.ext.intersphinx', 'sphinx.ext.viewcode', 'sphinx.ext.autosummary',
    'sphinx.ext.mathjax'
]

intersphinx_mapping = {'python': ('https://docs.python.org/3', None),
                       'numpy': ('https://docs.scipy.org/doc/numpy/', None),
                       'scipy': ('https://docs.scipy.org/doc/scipy/reference/', None),
                       'matplotlib': ('https://matplotlib.org/', None)}

plot_formats = [('png', 80)]
plot_html_show_formats = False
plot_html_show_source_link = False

autosummary_generate = True

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# Add any paths that contain templates here, relative to this directory.
#templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'



html_extra_path = ['../ISiTGRdemo.html']

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']


# -- Extension configuration -------------------------------------------------
