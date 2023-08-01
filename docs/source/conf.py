# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Náš "dračák"'
copyright = '2023, Jan Hutař'
author = 'Jan Hutař'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'cs'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# -- Options for LaTeX output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/latex.html

latex_engine = 'xelatex'
latex_elements = {
    'fontpkg': r'''
\setmainfont{DejaVu Serif}
\setsansfont{DejaVu Sans}
\setmonofont{DejaVu Sans Mono}
''',
    'preamble': r'''
%\setcounter{tocdepth}{2}
\setcounter{secnumdepth}{1}
''',
    'papersize': 'a5paper',
    'babel': r'\usepackage{babel}',
    'extraclassoptions': 'twoside',
    'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
}
