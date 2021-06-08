"""
In this module there are the classes that make up the backend of the template engine
"""

# We import class and method for build an abstract class
from abc import ABC, abstractmethod

## The tamplate engine abstract backend
# This is a backend interface for  further backend implementation and prototyping
# The goal of these backends is to add any setup needed to bind the bot with a template engine.


class Backend(ABC):
    @abstractmethod
    def render(self, template, *args, **kwargs) -> str:
        """
        Function that process and render a template with some context

        Parameters
        ----------
        template : str
            Template name

        Returns
        -------
        str
            Processed text
        """
        pass
