"""
In this module you will find some useful functions to render templates
"""
# We load the main engine
from ._loader import TemplateEngine

# and create a function to render a template directly
def render(template, **kwargs):
    # We intances to a templeta engine inside the function becouse
    # the function is made for be called when this template engine
    # is configured
    return TemplateEngine().render(template, **kwargs)
