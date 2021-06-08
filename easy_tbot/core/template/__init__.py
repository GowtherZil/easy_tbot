"""
This module is responsible for wrapping template 
engines to lower the complexity and separate the code of control from the messages we send
"""

# From experience we know that it is more productive to separate the code
# that represents the logic from the plain text that represents a message.
# Having a message of 40 lines in the middle of our logic would be a nuisance.
# That is why we include the template module.

# We import main class (TemplateEngine) as loader to outer scope
# this class handle all heavy lifting for the template engine
from ._loader import TemplateEngine as loader

# and some shortcut to
from ._shorcuts import render

# The *render* function allow us to render pretty fast a given template
