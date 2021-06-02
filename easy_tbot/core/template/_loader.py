"""
This module contains a class that works as a wrapper around the class
that we use as a template engine backend, making the backend not only accessible
but unique through a singleton pattern
"""
# We import classes needed to do some black magic with simultaneous meta classes
from abc import ABCMeta
# and the backend that we want inherit  from
from .backend import Backend
# This is our magic wand, allowing us to make a multi-meta class inheritance
from .._tools.meta import MultiMeta
# and a class that make his child a singleton objetc
from .._tools.meta_singleton import MetaSingleton
# and a class that make the  load process for us
from .._tools.generic_loader import GenericLoader

# ## The template engine main backend
# The main backend is a  template engine backend class that hold and expose inner backend class acting itself
# as a proxy and a wrapper to any backend implemented in the future 
class TemplateEngine(MultiMeta[ABCMeta, MetaSingleton, Backend, GenericLoader ]):
    """Class representing our template engine backend"""
    
    spected_class = Backend
    attribute = 'TEMPLATES'
    
    def render(self, template, *args, **kwargs):
        return self.wrapped.render(template, *args, **kwargs)