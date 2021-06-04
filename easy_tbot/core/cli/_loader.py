"""
This module contains a class that works as a wrapper around the class
that we use as a cli backend, making the backend not only accessible
but unique through a singleton pattern
"""

# We import ABCMeta class needed to a multi-meta inheritence (sort of black magic) in this module
from abc import ABCMeta

# and now a class that allow us some kind of advanced inspect or reflection
import inspect

# we import methods needed to dynamic import
from importlib import import_module

# and the backend that we want inherit  from
from .backend import Backend

# This is our magic wand, allowing us to make a multi-meta class inheritance
from .._tools.meta import MultiMeta

# and a class that make his child a singleton objetc
from .._tools.meta_singleton import MetaSingleton

# and a class that make the  load process for us
from .._tools.generic_loader import GenericLoader

# ## The CLI class
# The CLI class is the cli backend class that hold and expose inner backend class acting itself
# as a proxy and a wrapper to any backend implemented in the future
class CLI(MultiMeta[ABCMeta, MetaSingleton, Backend, GenericLoader]):
    """Class representing our cli backend"""

    spected_class = Backend
    attribute = "CLI"

    def shard_up(self, shard):
        """
        This method is for setup a shard of the bot
        used in the GenericLoader class

        Parameters
        ----------
        shard : str
            Represent a shard (this is a normal python module despite the cool name)
        """
        # a try to dynamically import the shard commands
        module = import_module(f"{shard}.commands")
        # and now we itterate over each member
        for name, value in inspect.getmembers(module, inspect.isclass):
            # then we instance that class, an we added as a command
            self.add_command(name, value())

    def add_command(self, name, command):
        return self.wrapped.add_command(name, command)

    def handle_input(self, *args):
        return self.wrapped.handle_input(*args)
