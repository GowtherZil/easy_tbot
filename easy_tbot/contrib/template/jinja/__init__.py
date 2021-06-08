"""
This module contains a template engine backend based on jinja2
"""

try:
    import jinja2
except:
    print(
        "Warning: Code in `easy_tbot.contrib.template.jinja` requires `jinja2>=2.11`."
    )
    print("FIX: You can install it with `pip install easy_tbot[jinja]`.")
    raise

from ._backend import JinjaBackend
