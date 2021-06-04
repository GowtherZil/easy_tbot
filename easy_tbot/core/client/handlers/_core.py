"""
The objective of this module is to create a series of class-based handlers 
that respond to functionalities that appear in almost all the libraries that 
surround the telegram bot api
"""
# We import the **ABC** module and the
# [Abstracthandler](ref:easy_tbot.core.bot.handlers.abstract:AbstractHandler)
# because they are the parent
# classes of these future handlers and we also import the **final** decorator
# to prevent the setup methods from changing with inheritance

from abc import ABC
from ._abstract import AbstractHandler
from typing import final

# ## The inline handler class
class InlineHandler(AbstractHandler, ABC):
    """
    This class know how setup an inline handler
    """

    @final
    def setup(self, bot):
        bot.add_inline_handler(
            self
        )  # check that this object(self) is the proper handler


# ## The chosen inline handler class
class ChosenInlineHandler(AbstractHandler, ABC):
    """
    This class know how setup a chosen inline handler
    """

    @final
    def setup(self, bot):
        bot.add_chosen_inline_handler(
            self
        )  # check that this object(slef) is the proper handler


# ## The message handler class
class MessageHandler(AbstractHandler, ABC):
    """
    This class know how setup a message handler
    """

    @final
    def setup(self, bot):
        bot.add_message_handler(self)


# ## The poll handler class
class PollHandler(AbstractHandler, ABC):
    """
    This class know how setup a poll handler
    """

    @final
    def setup(self, bot):
        bot.add_poll_handler(self)


# ## The poll answer handler class
class PollAnswerHandler(AbstractHandler, ABC):
    """
    This class know how setup a poll answer handler
    """

    @final
    def setup(self, bot):
        bot.add_poll_answer_handler(self)


# ## The call back query handler class
class CallbackQueryHandler(AbstractHandler, ABC):
    """
    This class know how setup a callback query handler
    """

    @final
    def setup(self, bot):
        bot.add_callback_query_handler(self)


# ## The shipping query handler class
class ShippingQueryHandler(AbstractHandler, ABC):
    """
    This class know how setup a shipping query handler
    """

    @final
    def setup(self, bot):
        bot.add_shipping_query_handler(self)


# ## The pre checkout query handler class


class PreCheckoutQueryHandler(AbstractHandler, ABC):
    """
    This class know how setup a pre checkout query handler
    """

    @final
    def setup(self, bot):
        bot.add_pre_checkout_query_handler(self)


# It is planned to make handlers for webhooks but for now it is up to you ;)
