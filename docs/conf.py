"""Configuration file for the Sphinx documentation builder.

More info at https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

project = "mobile_modem_exporter"
copyright = "2020, Thomas Steen Rasmussen"
author = "Thomas Steen Rasmussen"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx_rtd_theme",
    "sphinx.ext.napoleon",
    "sphinxarg.ext",
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
master_doc = "index"
version = "0.1.0-dev"
html_theme = "sphinx_rtd_theme"
html_theme_options = {"display_version": True}
man_pages = [
    (
        "mobile_modem_exporter",
        "mobile_modem_exporter",
        "Manpage for mobile_modem_exporter",
        ["Thomas Steen Rasmussen"],
        8,
    ),
]
manpages_url = "https://mobile-modem-exporter.readthedocs.io/en/latest/{page}.html"
napoleon_include_init_with_doc = True
