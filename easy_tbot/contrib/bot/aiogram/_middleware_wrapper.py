"""This module contains a class that works as a middleware in 
aiogram and helps us to integrate our own middlewares"""
# We import the base of the middlewares in aiogram
from aiogram.dispatcher.middlewares import BaseMiddleware
# **functools** to work with wrappers
import functools
# and **inspect** to do some reflection and instrocpection
import inspect

# ## The middleware wrappers
# This class works as a wrapper by converting our handler into an aiogram handler following an adapter pattern
class MiddlewareWrapper(BaseMiddleware):
    __middlewares = []

    def __init__(self, func):
        super().__init__()
        self.__func = func
        self.__class__.__middlewares.add_instance(func)
        functools.update_wrapper(self,self.__func)

    def setup(self, manager):
        self.__class__.__middlewares.append(self.__func)
        self._manager = manager

    def __getattribute__(self, name):
        if name == 'on_process_message':
            return self
        
        try:
            return super().__getattribute__(name)
        
        except AttributeError:
            return getattr(self.__func, name)
    
    def is_configured(self):
        return self.__func in self.__middlewares

    async def __call__(self, *args, **kwargs):
        if inspect.iscoroutinefunction(self.__func):
            return await self.__func(*args, **kwargs)
        return self.__func(*args, **kwargs)