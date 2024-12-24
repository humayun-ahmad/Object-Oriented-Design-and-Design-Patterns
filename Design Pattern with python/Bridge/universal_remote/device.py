from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    
    @abstractmethod
    def turn_off(self):
        pass
    
    @abstractmethod
    def increase_volume(self):
        pass
    
    @abstractmethod
    def decrease_volume(self):
        pass
    