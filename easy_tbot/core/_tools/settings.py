"""
This module contains the functionalities that allow us to access the configuration file of
our app.
"""

# We load the **os** modules to be able to access the environment variables,
import os

# and the **import_module** for do dynamically imports
from importlib import import_module

# we load **Callable** and **Any** for static typing
from typing import Callable, Any, final

# and logging for aplication loggin
import logging

# ## The Settings
# The **Settings**  class represents our configuration at runtime


@final
class Settings:
    """
    This class is intended as a wrapper around the configuration
    from an easy_tbot project.
    """

    # we create an initialization method
    def __init__(self, settings: dict = None):
        """
        Method that receives a configuration dictionary or nothing, in case it does not receive anything
        it will try to import the configuration module previously loaded in the environment variable BOT_SETTINIG_MODULE.

        Parameters
        ----------
        settings : dict, optional
            A configuration dictionary, by default None
        """
        if settings is None:
            self.__settings = import_module(os.environ.get("BOT_SETTING_MODULE"))
        else:
            self.__settings = settings

    # We overload the __getattribute__ method
    def __getattribute__(self, name):
        """
        This method is overwritten in order to first try to access its own attribute
        and otherwise return the attributes
        of the object that we are wrapping.

        Parameters
        ----------
        name : str
            Attribute name

        Returns
        -------
        Any
            Attribute value
        """

        try:
            return super().__getattribute__(name)  # Try to return own attribute
        except AttributeError:
            if isinstance(self.__settings, dict):
                return self.__settings[
                    name
                ]  # Try to return settings attribute if is a dictionary
            else:
                return getattr(
                    self.__settings, name
                )  # Try to return settings attribute to generic type

    # We create a method that serves as a bridge between each fragment
    # of the bot and each aspect of the framework allowing the latter
    # to configure the former

    def setup_shards(self, configurator: Callable[..., Any]):
        """
        This method iterates over the different fragments of
        the bot to configure them with another external function which we call
        'configurator'

        Parameters
        ----------
        configurator : Callable[..., Any]
            A function that can configure one single shard

        Raises
        ------
        Exception
            This method can broadcast up exceptions raised by the configurator
        """
        # We are aware that this must be improved
        setup = logging.getLogger("tbot")  # We setup the logger

        for shard in self.SHARDS:  # itterate over shards
            try:
                configurator(shard)  # and then call external configurator over shards
            except ImportError as e:  # Some configurators try to import stuff from shard and fail
                setup.log(
                    logging.WARNING, str(e)
                )  # This must be informed as a warning and can be ignored
            except Exception as e:
                setup.log(
                    logging.ERROR, str(e)
                )  # No other type of exception is expected, therefore they are reported as an error
                raise e  # and raise as exception later
