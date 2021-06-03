"""
This module implements a generic decorator factory that 
will be used later to create specific decorators around our handlers.
"""

# We import this for future abstract class creation
from abc import ABC
# import inspect module for some dynamic check
import inspect
# and the update_wrapper method for do that 😑 'update a wrapper'  😑
from functools import  update_wrapper
# this is used in some further  black magic
from ..handlers import AbstractHandler

# ## The factory 🏭
# At first we created the decorators one by one but found 
# it to be a bunch of repeating code. We created the factory 
# to encapsulate or try to encapsulate that repeated code and apparently we succeeded.

def create_decorator(base_class, *args, **kwargs):
    """This class creates decorators that are configured in specific ways in the backend

    Parameters
    ----------
    base_class : SetupMixing
        Base class used to setup something in the bot

    Returns
    -------
    Callable
        A new decorator with a proper behavior
    """    

    def decorator(f):
        """
        The decorator that we dynamically create 

        Parameters
        ----------
        f : Callable
            The object that we can decorate

        Returns
        -------
        SetupMixing
            A SetupMixing that has a behavior and can be setup for specific things
        """        

        # Now we create a class that acts as a wrapper for 
        # the function that we pass by parameters to the decorator.
        # This class can be configured in a bot backend depending on the
        # base configuration class that we pass to the factory.
        class Wrapper(AbstractHandler, ABC):
            """
            A generic wrapper class            
            """
            
            def __init__(self):
                # We update the wrapper of decorated function
                update_wrapper(self, f)

            @property
            def meta(self)->dict:
                d = {'args':args}
                d.update(kwargs)
                return d
                
            def setup(self, bot):                
                return base_class.setup(self, bot)
        

        # Now we implement two classes for the different types of 
        # methods that we can find


        class AsyncWrapper(Wrapper):
            """
            A class for decorate an async method
            """

            async def __call__(self, *args, **kwargs):
                """
                The propper call for async method instance

                Returns
                -------
                None
                """                
                return await f(*args, **kwargs)

        class SyncWrapper(Wrapper):            
            """
            A class for decorate sync methods
            """
            def __call__(self, *args, **kwargs):
                """
                The propper call for sync method instance

                Returns
                -------
                None
                """                
                return f(*args, **kwargs)

        # We check the type of function and return a class accordingly
        return AsyncWrapper if inspect.iscoroutinefunction(f) else SyncWrapper
    return decorator
