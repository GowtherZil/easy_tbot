"""
This module is responsible for wrapping template 
engines to lower the complexity and separate the code of control from the messages we send
"""

# From experience we know that it is more productive to separate the code
# that represents the logic from the plain text that represents a message.
# Having a message 40 lines in the middle of our logic would be a nuisance.
# That is why we include the template module, to separate our logic from plain
# text.

# We import some shorcut function

from ._shorcuts import render
from ._loader import TemplateEngine as loader
