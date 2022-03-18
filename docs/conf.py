import sys
from pathlib import Path


DOC_ROOT = Path(__file__).parent.absolute()
sys.path.extend([str(DOC_ROOT/'utils'),
                 str(DOC_ROOT.parent/'src')])


# -- Project information -----------------------------------------------------

project = 'Pytorch Book'
copyright = '2022, xinetzone'
author = 'xinetzone'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_nb',
    'sphinx_copybutton',
    'sphinx_tabs.tabs',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.napoleon',
    'sphinxcontrib.bibtex',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = [f'{DOC_ROOT}/_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pytorch_book'
html_theme_path = [f'{DOC_ROOT}/../src/themes']

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = [f'{DOC_ROOT}/_static']
html_css_files = ["default.css"]

html_logo = f'{DOC_ROOT}/_static/images/logo.jpg'
# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = f'{DOC_ROOT}/_static/images/favicon.jpg'
html_baseurl = 'https://xinetzone.github.io/pytorch-book'

html_last_updated_fmt = '%Y-%m-%d, %H:%M:%S'

# MyST-NB 设置
# 如果你希望stderr和stdout中的每个输出都被合并成一个流，请使用以下配置。
# 避免将 jupter 执行报错的信息输出到 cmd
nb_merge_streams = True
execution_allow_errors = True
jupyter_execute_notebooks = "off"

nb_render_priority = {
    "html": (
        "application/vnd.jupyter.widget-view+json",
        "application/javascript",
        "text/html",
        "image/svg+xml",
        "image/png",
        "image/jpeg",
        "text/markdown",
        "text/latex",
        "text/plain",
    ),
    'gettext': ()
}

# -- 国际化输出 ----------------------------------------------------------------
gettext_compact = False
locale_dirs = ['../locales/']

# Napoleon 设置
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = True
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = True
napoleon_type_aliases = None
napoleon_attr_annotations = True

# ``pydata-sphinx-theme`` 配置
autosummary_generate = True
html_theme_options = {
    "footer_items": ["copyright", "last-updated", "sphinx-version", ],
    "github_url": "https://github.com/xinetzone/pytorch-book",
    "use_edit_page_button": True,
    "external_links": [
      {"name": "API", "url": f"{html_baseurl}/api"},
  ]
}

html_context = {
    "github_user": "xinetzone",
    "github_repo": "pytorch-book",
    "github_version": "main",
    "doc_path": "docs",
}

bibtex_bibfiles = [f'{DOC_ROOT}/refs.bib']
bibtex_reference_style = "author_year"

intersphinx_mapping = {
    'python': ('https://daobook.github.io/cpython/', None),
    'sphinx': ('https://daobook.github.io/sphinx/', None),
    'peps': ('https://daobook.github.io/peps', None),
    'pytorch': ('https://pytorch.org/docs/stable', None),
    'pytorchx': (f"{html_baseurl}/api", None),
    'torchvision': ('https://pytorch.org/vision/stable', None),
    'torchtext': ('https://pytorch.org/text/stable/', None),
    'torchaudio': ('https://pytorch.org/audio/stable/', None)
}
