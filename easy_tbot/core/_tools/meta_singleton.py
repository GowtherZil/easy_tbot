"""
This module contains a single class that implements 
the singleton pattern for those classes that have it as a metaclass.
"""
# ## The meta singleton

# The idea is that the backend and other classes that
# run our bot are instantiated only once and for that we use the well-known singleton pattern


class MetaSingleton(type):
    """
    Metaclass representing a singleton,
    we achieve this by mapping each child class
    type with its first instance
    """

    instances = {}

    def __call__(cls, *args, **kwargs):
        """Where the class is instantiated

        Returns
        -------
        MetaSingleton
            A class that follows a singleton pattern
        """
        if not cls in cls.instances:  # map it if this class hasn't been mapped yet
            cls.instances[cls] = super().__call__(*args, **kwargs)
        return cls.instances[cls]  # return the saved instance
