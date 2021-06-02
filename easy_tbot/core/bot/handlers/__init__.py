"""
This module is in charge of defining the shape of the handlers when it is a class.
"""

# The framework not only thinks of making handles that are isolated in function form,
# we think that isolating them using classes can give us one more layer to encapsulate 
# the logic of a handle.

"""This module may undergo serious expansions in the future."""

# Importing core handlers as shortcut
from .abstract import AbstractHandler
from .core import (MessageHandler, InlineHandler, 
ChosenInlineHandler, PollHandler, PollAnswerHandler,
CallbackQueryHandler, ShippingQueryHandler, PreCheckoutQueryHandler)
