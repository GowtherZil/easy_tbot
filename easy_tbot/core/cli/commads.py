
# Import class and method decorator for build  abstract classes
from abc import ABC, abstractmethod
# and some static type
from typing import Any

# ## The CLI command
# The purpose of the class is to have the representation of a command in the form of a class
class CliCommand(ABC):
    """
    Represents a command used in the OS shell
    """
    
    @abstractmethod
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return self.do(*args, **kwargs)