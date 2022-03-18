import sys
from pathlib import Path


DOC_ROOT = Path(__file__).parent.absolute()
sys.path.extend([str(DOC_ROOT.parent/'src'),
                 str(DOC_ROOT.parent/'docs'),
                 ])

from conf import *

# -- 国际化输出 ----------------------------------------------------------------
gettext_compact = False
locale_dirs = ['../locales/']

html_theme_options.update(
    {
        "external_links": [
            {"name": "文档", "url": html_baseurl},
        ]
    }
)
