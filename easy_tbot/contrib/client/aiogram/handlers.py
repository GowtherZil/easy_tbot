"""This module contains specific handlers for aiogram backend"""

# We import **final** for protect methods in inheritance
from typing import final
# and the [AbstractHandler](ref:easy_tbot.core.bot.handler.abstract:AbstractHandler) class
# to inherit from her
from easy_tbot.core.client.handlers import AbstractHandler

# ## The aiogram handlers

# for chanel post
class ChanelPostHandler(AbstractHandler):
    @final
    def setup(self, bot):
        bot.add_chanel_post_handler(self)

# for edited chanel post
class EditedChanelPostHandler(AbstractHandler):
    @final
    def setup(self, bot):
        bot.add_edited_chanel_post_handler(self)

# for middlewares
class Middleware(AbstractHandler):
    @final
    def setup(self, bot):
        bot.add_middleware(self)