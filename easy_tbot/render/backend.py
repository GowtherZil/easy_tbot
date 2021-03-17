from abc import ABC, abstractmethod

class Backend(ABC):

    @abstractmethod
    def render(self, template, *args,  **kwargs):
        pass