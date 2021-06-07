"""
This module contains the structures and functions that allow us to wrap
another module or library that can create connections with the telegram 
bots api.
"""

# This module is in charge of wrapping classes like aiogram or pyTelegramBotApi.
# In it, a series of objects is created that make a bridge between the
# specifications of the framework and the library that it wraps.

# We import main class (Clien) as loader to outer scope
# this class handle all heavy lifting for the client bot
from ._loader import Client as loader
