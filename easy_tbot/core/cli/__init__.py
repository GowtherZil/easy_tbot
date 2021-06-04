"""
Module where we define objects and functions to handle the cli in developer mode
"""

# Sometimes when we make a bot we want to automate some things and as developers we make
# small scripts to do it, the idea would be those automations
# (many times related to deployment) to do them through a command,
# other times we want useful commands such as running our bot from the cli,
# for those things this module was developed.

from ._loader import CLI as loader
