"""
This module contains specific decorators for aiogram backend
"""

# We import the
# [create_decorator](ref:easy_tbot.core.bot.decorators.decorator_factory:create_decorator)
# method for easing our life
from easy_tbot.core.client.decorators import create_decorator

# and the related handler for creating the decorators
from .handlers import ChanelPostHandler, EditedChanelPostHandler, Middleware

# ## The aiogram decorators

# to handler chanel post
def chanel_post_handler(*args, **kwargs):
    return create_decorator(ChanelPostHandler, *args, **kwargs)


# to handler edited chanel post
def edited_chanel_post_handler(*args, **kwargs):
    return create_decorator(EditedChanelPostHandler, *args, **kwargs)


# to act like a middleware
def middleware(*args, **kwargs):
    return create_decorator(Middleware, *args, **kwargs)
