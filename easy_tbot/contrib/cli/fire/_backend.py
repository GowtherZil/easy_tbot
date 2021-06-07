"""
This module contains the cli backend implementation based on fire
"""

# We import our [cli backend](ref:easy_tbot.core.cli.backend:Backend)
from easy_tbot.core.cli.backend import Backend

# and the module that we will use for create the backend
import fire

# ## The FireBackend
# This backend use a dict of objetcs and **fire** module for handle commands
class FireBackend(Backend):
    """
    Handles all commands and stuff of every base or created section in the bot
    """

    def __init__(self) -> None:
        super().__init__()
        self.__commands = {}

    def add_command(self, name, command):
        """
        Adds a command to the handler
        :param command: Command to add
        :return: None
        """
        self.__commands[name] = command

    def handle_input(self, *args):
        """
        Process the OS command input
        :param args:
        :return:
        """
        fire.Fire(self.__commands)
