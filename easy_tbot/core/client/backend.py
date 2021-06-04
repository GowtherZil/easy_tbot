"""
This module contains the interfaces or abstract classes that allow to implement proxies 
that function as bridges between the framework and the telegram client libraries.
"""

# We import class and method needed to do a python abstract class
from abc import ABC, abstractmethod

# ## Bot backend prototype
# The class is a skeleton, a prototype or abstract class that serves as a guide to the child classes
class Backend(ABC):
    """
    A very base bot backend class
    """

    @abstractmethod
    def add_message_handler(self, handler):
        """
        This method must add a message handler to our bot backend
        """
        pass

    @abstractmethod
    def add_inline_handler(self, handler):
        """
        This method must add an inline handler to our bot backend
        """
        pass

    @abstractmethod
    def add_chosen_inline_handler(self, handler):
        """
        This method must add a chosen inline handler to our bot backend
        """
        pass

    @abstractmethod
    def add_callback_query_handler(self, handler):
        """
        This method must add a callback query handler to our bot backend
        """
        pass

    @abstractmethod
    def add_shipping_query_handler(self, handler):
        """
        This method must add a shipping query handler to our bot backend
        """
        pass

    @abstractmethod
    def add_pre_checkout_query_handler(self, handler):
        """
        This method must add a pre checkout query handler to our bot backend
        """
        pass

    @abstractmethod
    def add_poll_handler(self, handler):
        """
        This method must add a poll handler to our bot backend
        """
        pass

    @abstractmethod
    def add_poll_answer_handler(self, handler):
        """
        This method must add a poll answer handler to our bot backend
        """
        pass

    @abstractmethod
    def run(self, *args, **kwargs):
        """
        Method in charge of start our backend
        """
        pass


# !!! note
#     This class can be extended in future releases in order to add new features to our bot
