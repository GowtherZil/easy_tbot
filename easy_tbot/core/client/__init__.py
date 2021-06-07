"""
This module contains the structures and functions that allow us to wrap
another module or library that can create connections with the telegram 
bots api.
"""

# The first idea that came to our mind was 
# 'let's create a telegram client ourselves' 
# but there were so many of these created that we had a second idea 
# 'let's wrap telegram clients'
# We define inside this  a series of objects is created that make a bridge between the
# specifications of the framework and the library that it wraps.

# We import main class (Clien) as loader to outer scope
# this class handle all heavy lifting for the client bot
from ._loader import Client as loader
