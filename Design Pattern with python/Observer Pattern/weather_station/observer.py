from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self):
        pass
    
class TemperatureDisplay(Observer):
    def __init__(self, name):
        self._name = name
        self._temperature = None
    
    def update(self, temperature):
        self._temperature = temperature
        print(f"{self._name} updated: Temperature is now {self._temperature}°C.")
        
    