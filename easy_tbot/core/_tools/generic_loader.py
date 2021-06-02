"""
This module encapsulate common code for every loader in the framework
"""

# We import some related exception to raise when we can´t load the settings
from easy_tbot.core.exceptions import WrongSettingsException
# and the setting class needed to proper setup and load the class
from easy_tbot.core._tools.settings import Settings

# ## The generic loader
# The generic loader is a class made mainly to encapsulate a small amount
#  of code that almost all backends have in common.
class GenericLoader:
    """
    This class work as a generic loader that search for some 
    attribute in settings module and check if is instance of a spected_class
    """
    spected_class:type
    attribute:str

    def __init__(self):
         # we create a settings instance making sure it loads from the environment
        settings = Settings()

        # and check if settings has DB attribute
        if not hasattr(settings, self.attribute):
            raise WrongSettingsException(f'{self.attribute} attribute missing in "settings.py" file')

        # We check if settings has CLI['backend'] attribute with the correct type
        if not isinstance(getattr(settings, self.attribute), self.spected_class):
            raise WrongSettingsException('Database backend has incorrect parent class')
        
        # if we reach this point we just use our instance class
        self.__wrapped = getattr(settings, self.attribute)

        if hasattr(self, 'shard_up'):
            settings.setup_shards(getattr(self, 'shard_up'))
    

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
           
            if hasattr(self, 'wrapped') and self.wrapped is not None:
                return getattr(self.wrapped, name)
            else:
                raise e
