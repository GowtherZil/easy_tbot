"""
This module contains a class that works as a wrapper around the class
that we use as a bot backend, making the backend not only accessible
but unique through a singleton pattern
"""

# We import classes needed to do some black magic with simultaneous meta classes
from abc import ABCMeta

# and now a class that allow us some kind of advanced inspect or reflection
import inspect

# we import methods needed to dynamic import
from importlib import import_module

# and the backend that we want inherit  from
from .backend import Backend

# the [AbstractHandler](ref:easy_tbot.core.bot.handlers.abstract:AbstractHandler) class
# for some type check
from .handlers import AbstractHandler

# This is our magic wand, allowing us to make a multi-meta class inheritance
from .._tools.meta import MultiMeta

# and a class that make his child a singleton objetc
from .._tools.meta_singleton import MetaSingleton

# and a class that make the  load process for us
from .._tools.generic_loader import GenericLoader

# ## The main Bot backend
# The main Bot backend is a super bot backend class that hold and expose inner backend class acting itself
# as a proxy and a wrapper to any backend implemented in the future


class Client(MultiMeta[ABCMeta, MetaSingleton, Backend, GenericLoader]):
    """Class representing our bot backend"""

    spected_class = Backend
    attribute = "BOT"

    def shard_up(self, shard):
        """
        This method is for setup a shard of the bot.
        Used in GenericLoader class

        Parameters
        ----------
        shard : str
            Represent a shard (this is a normal python module despite the cool name)
        """
        # a try to dynamically import the shard handlers
        lmodule = import_module(f"{shard}.handlers")

        # and now we itterate over each member
        for name, value in inspect.getmembers(lmodule, inspect.isclass):
            # and checkout if a member is a setup mixing and is not an abstract class.
            if issubclass(value, AbstractHandler) and not inspect.isabstract(value):
                # then we instance that class, as a  class of SetupMixing
                # a instance must know how setup a class in a bot backend
                # and we call setup function for do that
                value().setup(self)

    # We implement each method of the Backend class exposing the mothods of the class we wrap

    def add_message_handler(self, message_handler):
        return self.wrapped.add_message_handler(message_handler)

    def add_inline_handler(self, inline_handler):
        return self.wrapped.add_inline_handler(inline_handler)

    def add_chosen_inline_handler(self, chosen_inline_handler):
        return self.wrapped.add_chosen_inline_handler(chosen_inline_handler)

    def add_callback_query_handler(self, callback_query_handler):
        return self.wrapped.add_callback_query_handler(callback_query_handler)

    def add_shipping_query_handler(self, shipping_query_handler):
        return self.wrapped.add_shipping_query_handler(shipping_query_handler)

    def add_pre_checkout_query_handler(self, pre_checkout_query_handler):
        return self.wrapped.add_pre_checkout_query_handler(pre_checkout_query_handler)

    def add_poll_handler(self, poll_handler):
        return self.wrapped.add_poll_handler(poll_handler)

    def add_poll_answer_handler(self, poll_answer_handler):
        return self.wrapped.add_poll_answer_handler(poll_answer_handler)

    def run(self, *args, **kwargs):
        return self.wrapped.run(*args, **kwargs)
