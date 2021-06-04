"""
Very base module for every handler
"""

# We import **ABC** class and **abstractmethod** to define some interface or abstract class
# to ours class handler
from abc import ABC, abstractmethod

# and a class for works with regular expresions
import re

# ## The abstract handler
# The class is made to maintain a development line, a prototype,
# a standard for future implementations


class AbstractHandler(ABC):
    """
    Class that define what every handler must override
    """

    @property
    def meta(self):
        r = r"__\w+__"  # a regular expresion for private atttributes
        if hasattr(self, "Meta"):
            return {
                key: val
                for key, val in getattr(self, "Meta").__dict__.items()
                if not re.match(r, key)
            }
        return {}

    @abstractmethod
    def __call__(self, *args, **kwargs):
        """
        This method must be overridden to handle an update or information coming
        from the bot
        """
        pass

    @abstractmethod
    def setup(self, bot):
        """
        A setup method tha know how setup this class using the base class setup

        Parameters
        ----------
        bot : easy_tbot.bot.backend.Backend
            the bot backend to setup

        Returns
        -------
        None
        """
        pass
