"""This module contains the implementation of the bot backend based on aiogram"""

# We import **typing**  module for do some static typing
import typing

# now we import the classes that let us use aiogram freele as a backend
from aiogram import Bot, Dispatcher, executor

# now we import our [bot backend](ref:easy_tbot.core.bot.backend:Backend)
# to inherit from it
from easy_tbot.core.client.backend import Backend

# We import the [AbstractHandler](ref:easy_tbot.core.bot.handler.abstract:AbstractHandler) class
# for some static check
from easy_tbot.core.client.handlers import AbstractHandler

# and this [middleware wrapper](ref:easy_tbot.contrib.bot.aiogram.middleware_wrapper:MiddlewareWrapper)
from ._middleware_wrapper import MiddlewareWrapper

# ## The Aiogram Backend
# It is an implementation based on a composite and adapter pattern using aiogram objects
class AiogramBackend(Backend):
    def __init__(self, *args, **kwargs):

        self.__skip_updates = False
        if "skip_updates" in kwargs:
            self.__skip_updates = kwargs["skip_updates"]
            del kwargs["skip_updates"]

        self.__bot = Bot(*args, **kwargs)
        self.__dispatcher = Dispatcher(self.__bot)

    @property
    def bot(self):
        return self.__bot

    @property
    def dispatcher(self):
        return self.__dispatcher

    @staticmethod
    def __add(handler: AbstractHandler, decorator: typing.Callable):
        # for function , class compatibility
        kwargs = handler.meta
        args = kwargs.pop("args", [])
        if not args:
            args = kwargs.pop("custom_filters", [])
        return decorator(*args, **kwargs)(handler)

    def add_middleware(self, handler):
        self.dispatcher.setup_middleware(MiddlewareWrapper(handler))

    def add_message_handler(self, handler):
        decorator = self.dispatcher.message_handler
        return self.__add(handler, decorator)

    def add_edited_message_handler(self, handler):
        decorator = self.dispatcher.edited_message_handler
        return self.__add(handler, decorator)

    def add_chanel_post_handler(self, handler):
        decorator = self.dispatcher.channel_post_handler
        return self.__add(handler, decorator)

    def add_edited_chanel_post_handler(self, handler):
        decorator = self.dispatcher.edited_channel_post_handler
        return self.__add(handler, decorator)

    def add_inline_handler(self, handler):
        decorator = self.dispatcher.inline_handler
        return self.__add(handler, decorator)

    def add_chosen_inline_handler(self, handler):
        decorator = self.dispatcher.chosen_inline_handler
        return self.__add(handler, decorator)

    def add_callback_query_handler(self, handler):
        decorator = self.dispatcher.callback_query_handler
        return self.__add(handler, decorator)

    def add_shipping_query_handler(self, handler):
        decorator = self.dispatcher.shipping_query_handler
        return self.__add(handler, decorator)

    def add_pre_checkout_query_handler(self, handler):
        decorator = self.dispatcher.pre_checkout_query_handler
        return self.__add(handler, decorator)

    def add_poll_handler(self, handler):
        decorator = self.dispatcher.poll_handler
        return self.__add(handler, decorator)

    def add_poll_answer_handler(self, handler):
        decorator = self.dispatcher.poll_answer_handler
        return self.__add(handler, decorator)

    def run(self, *args, **kwargs):
        return executor.start_polling(self.dispatcher, skip_updates=self.__skip_updates)
