"""
This module contains a set of decorators that work as other decorators 
work in pyTelegramBotApy, Telethon, Aiogram etc. Converting our methods 
into specific handlers of the updates that Telegram makes to our bot.
"""

# We import all the handlers as a shortcut
from .decorator_factory import create_decorator
from .core import (
    inline_handler, 
    chosen_inline_handler, 
    message_handler,
    poll_answer_handler, 
    poll_handler, 
    callback_query_handler, 
    pre_checkout_query_handler,
    shipping_query_handler
    )
