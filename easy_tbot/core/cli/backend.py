"""
In this module there are the classes that make up the backend of the CLI
"""

# We import class and method decorator for build  abstract classes
from abc import ABC, abstractmethod

# and the command class for static typing
from .commads import CliCommand

# ## The CLI Backend

# A backend interface for  further backend implementation and prototyping
# The goal of these backends is to be able to enter commands and handle user
# input


class Backend(ABC):
    """
    A backend of a command handler
    """

    @abstractmethod
    def add_command(self, name, command: CliCommand):
        """
        This method is responsible for adding a command

        Parameters
        ----------
        command : ShellCommand
            A shell command
        """
        pass

    @abstractmethod
    def handle_input(self, *args):
        """
        This method is responsible for handle a user input
        """
        pass
