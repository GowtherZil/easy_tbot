"""
In this module as in others in this same namespace we
create decorators for specific handlers, in this case
those that are related to the core handlers.
"""
# we start as other times importing the core function for do this
from .decorator_factory import create_decorator
# and now we import the base class for our decorators 
from ..handlers import InlineHandler, ChosenInlineHandler, MessageHandler,\
    CallbackQueryHandler, PollAnswerHandler, PollHandler, PreCheckoutQueryHandler,\
    ShippingQueryHandler

# ## Core decorators
# We start creating decorartors that handle data throwed to our bot

def inline_handler(*args, **kwargs):
    """
    Decorate a function to handle inlines

    Returns
    -------
    Callable
        A decorator
    """    
    return create_decorator(InlineHandler, *args, **kwargs)

def chosen_inline_handler(*args, **kwargs):
    """
    Decorate a function to handle chosen inlines

    Returns
    -------
    Callable
        A decorator
    """    
    return create_decorator(ChosenInlineHandler, *args, **kwargs)

def message_handler(*args, **kwargs):
    """
    Decorate a function to handle messages

    Returns
    -------
    Callable
        A decorator
    """      
    return create_decorator(MessageHandler, *args, **kwargs)


def poll_handler(*args, **kwargs):
    """
    Decorate a function to handle polls

    Returns
    -------
    Callable
        A decorator
    """      
    return create_decorator(PollHandler, *args, **kwargs)

def poll_answer_handler(*args, **kwargs):
    """
    Decorate a function to handle polls answer

    Returns
    -------
    Callable
        A decorator
    """  
    return create_decorator(PollAnswerHandler, *args, **kwargs)

def callback_query_handler(*args, **kwargs):
    """
    Decorate a function to handle querys callbacks

    Returns
    -------
    Callable
        A decorator
    """      
    return create_decorator(CallbackQueryHandler, *args, **kwargs)

def shipping_query_handler(*args, **kwargs):
    """
    Decorate a function to handle shiping querys

    Returns
    -------
    Callable
        A decorator
    """      
    return create_decorator(ShippingQueryHandler, *args, **kwargs)

def pre_checkout_query_handler(*args, **kwargs):
    """
    Decorate a function to handle pre checkout querys 

    Returns
    -------
    Callable
        A decorator
    """      
    return create_decorator(PreCheckoutQueryHandler, *args, **kwargs)