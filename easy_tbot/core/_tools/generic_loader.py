"""
This module encapsulate common code for every loader in the framework
"""

# We import some related exception to raise when we can´t load the settings
from easy_tbot.core.exceptions import WrongSettingsException

# and the setting class needed to proper setup and load the class
from easy_tbot.core._tools.settings import Settings

# we import inspect for do some code reflection
import inspect 

from importlib import import_module

# ## The generic loader
# The generic loader is a class made mainly to encapsulate a small amount
#  of code that almost all backends have in common.
class GenericLoader:
    """
    This class work as a generic loader that search for some
    attribute in settings module and check if is instance of a spected_class
    """

    spected_class: type
    attribute: str

    def __init__(self):
        # we create a settings instance making sure it loads from the environment
        settings = Settings()

        # and check if settings has DB attribute
        if not hasattr(settings, self.attribute):
            raise WrongSettingsException(
                f'{self.attribute} attribute missing in "settings.py" file'
            )

        target =  getattr(settings, self.attribute)
        module, class_ = self.__module_and_class(target['backend'])
        backend = getattr(import_module(module), class_)
        config = target['config']
        
        # We check if settings has CLI['backend'] attribute with the correct type
        if not issubclass(backend, self.spected_class):
            raise WrongSettingsException(f"{self.attribute} backend has incorrect parent class")

        # if we reach this point we just use our instance class
        self.__wrapped = backend(**config)

        if hasattr(self, "shard_up"):
            settings.setup_shards(getattr(self, "shard_up"))

    @property
    def wrapped(self):
        return self.__wrapped

    def __getattribute__(self, name: str):
        """
        We override this to expose the attributes of the instance of the class we wrap

        Parameters
        ----------
        name : str
            Attribute name

        Returns
        -------
        Any
            Attribute value if any
        """
        try:
            return super().__getattribute__(name)

        except AttributeError as e:

            if hasattr(self, "wrapped") and self.wrapped is not None:
                return getattr(self.wrapped, name)
            else:
                raise e

    def __module_and_class(self, path:str):
        """Return module and class for a full class path

        Parameters
        ----------
        path : str
            Full path of a class definition

        Returns
        -------
        tuple
            module, class
        """        
        data = path.split('.')
        _class = data[-1]
        module = ''
        for x in data[:-1]:
            module+=f'{x}.'
        return module[:-1], _class


