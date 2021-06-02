"""
In this module are the core functionalities of the framework.
"""

# The idea is to have four private classes, one for each main functionality 
# (one for the bot, one for the databases, another for the template 
# engine and another for the cli), 
# these classes would be the administrators 
# and at the same time they would delegate part 
# of their implementation to future developers. We achieve 
# this by mixing various design patterns, specifically the 
# proxy, adpater, and singleton pattern. These classes work as a 
# singleton that act as proxies and adapters between the classes 
# that are created in the future and the framework. Each of these classes 
# takes care of part of the heavy lifting of the bot having as input the 
# class in charge of the CLI most of the time.

from ._tools.settings import Settings