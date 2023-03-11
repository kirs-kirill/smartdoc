# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'smart-doc'
copyright = '2023, usem'
author = 'usem'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.imgconverter",
    "sphinx_inline_tabs",
    "sphinx_copybutton",
]

templates_path = ['_templates']
exclude_patterns = []

language = 'ru'

html_show_sphinx = False


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = ('furo')
html_static_path = ['_static']
html_title = "Документация SmartEngin"
html_theme_options = {
    "prev_next_buttons_location": "both",
    "navigation_with_keys": True,
    "top_of_page_button": None,
    # "announcement": "",
    "light_css_variables": {
        "color-brand-primary": "#336790",  # "blue"
        "color-brand-content": "#336790",
    },
    "dark_css_variables": {
        "color-brand-primary": "#E5B62F",  # "yellow"
        "color-brand-content": "#E5B62F",
    },
}

epub_language = 'ru'
epub_title = 'smart-doc'
epub_author = 'usem'
epub_publisher = 'usem'
epub_copyright = '2023, usem'