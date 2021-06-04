"""
This module expose a shortcut for command handling
"""

# We import the CLI main module called loader in outer scopes
from ._loader import CLI

# and now we implement the handle shortcut
def handle(*args):
    CLI().handle_input(*args)
