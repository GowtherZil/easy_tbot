"""
This module is in charge of defining the shape of the handlers when it is a class
"""

# The framework not only thinks of making handles that are isolated in function form,
# we think that isolating them using classes can give us one more layer to encapsulate 
# the logic of a handle.

from ._abstract import AbstractHandler
from ._core import (MessageHandler, InlineHandler, 
ChosenInlineHandler, PollHandler, PollAnswerHandler,
CallbackQueryHandler, ShippingQueryHandler, PreCheckoutQueryHandler)

