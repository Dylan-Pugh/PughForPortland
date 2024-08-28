# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Dylan Pugh for HD 114'
copyright = '2024, Portland Neighbors for Dylan Pugh. Authorized by the candidate'
author = 'Dylan Pugh'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser', 'sphinx_design', 'ablog', 'sphinx.ext.intersphinx']
myst_enable_extensions = ["colon_fence"]
myst_update_mathjax = False

templates_path = ['_templates']
exclude_patterns = [
    ".github/*",
    ".history",
    "github_submodule/*",
    "LICENSE.md",
    "README.md",
]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.

html_logo = "_static/logos/DylanPugh_Logos-06A.png"
html_show_sourcelink = False
html_copy_source = False
#html_permalinks = False

html_theme_options = {
    # https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/header-links.html#fontawesome-icons
    "icon_links": [
        {
            "name": "Instagram",
            "url": "https://instagram.com/pughfoundation",
            "icon": "fa-brands fa-instagram",
        },
        {
            "name": "GitHub",
            "url": "https://github.com/Dylan-Pugh",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "Voter Resources",
            "url": "https://www.maine.gov/sos/cec/elec/voter-info/voterguide.html",
            "icon": "fa-solid fa-check-to-slot",
        },
    ],
     "external_links": [
        {"name": "Contact Me", "url": "mailto:inquiry@pughforportland.org"},
        {"name": "Donate on ActBlue", "url": "https://secure.actblue.com/donate/pugh-for-portland"},
    ],
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["navbar-icon-links"],
    "navbar_persistent": [],
    "header_links_before_dropdown": 4,
    "show_prev_next": False,

    "announcement": "<a href='https://secure.actblue.com/donate/pugh-for-portland' class='homepage-button primary-button'>Donate Today!</a>"
}


html_context = {
    "default_mode": "light",
}


html_title = 'Dylan Pugh for HD114'

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/favicon.svg"


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
html_static_path = ["_static"]
html_css_files = ["custom.css"]


source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# -- Blog configuration ---------------------------------------------------
# https://ablog.readthedocs.io/en/stable/manual/ablog-configuration-options.html

blog_path = 'blog'
blog_title = 'Updates from Dylan'
blog_baseurl = 'pughforportland.org'
blog_authors = {
    'Dylan': ('Dylan Pugh', 'pughforportland.org'),
}
blog_default_author = 'Dylan'

html_sidebars = {
    "issues": [],
    "blog": [],
   'blog/*': [
          'ablog/postcard.html', 'ablog/recentposts.html',
          'ablog/categories.html',
         ]
}