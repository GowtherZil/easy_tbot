from abc import ABC, abstractmethod

class Backend(ABC):

    @abstractmethod
    def add_command(self, command):
        pass

    @abstractmethod
    def add_commands(self, *args):
        pass

    @abstractmethod
    def handle_input(self, *args):
        pass

    @abstractmethod
    def type_is_command(self, type_obj)->bool:
        pass