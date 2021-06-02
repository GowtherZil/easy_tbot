"""
In this module there are the classes that make up the backend of the databases
"""

# Import class and method for build an abstract class
from abc import ABC, abstractmethod

# ## The database abstract backend
# A backend interface for  further backend implementation and prototyping
# The goal of these backends is to add any setup needed to bind the bot with a database.
class Backend(ABC):
    """
    A base class for databases backends
    """    
    
    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass