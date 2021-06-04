"""
This module contains decorators to create commands
"""

# We import this utility to handle wrappers shaped like objects
from functools import update_wrapper

# and the command base
from easy_tbot.core.cli.commads import CliCommand

# ## The decorator
# The decorator creates a ClICommand class (without instantiating)
# around the function and exposes the function as a callable object


def command(f):
    class CommandWrapper(CliCommand):
        def __init__(self) -> None:
            super().__init__()
            self.__f = f
            update_wrapper(self, self.__f)

        def __call__(self, *args, **kwargs):
            return self.__f(*args, **kwargs)

    return CommandWrapper
