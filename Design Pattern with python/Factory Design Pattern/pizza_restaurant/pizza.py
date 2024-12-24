from abc import ABC, abstractmethod

class Pizza(ABC):
    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def bake(self):
        pass

    @abstractmethod
    def box(self):
        pass

class MargheritaPizza(Pizza):
    def prepare(self):
        print("Preparing Margherita Pizza")

    def bake(self):
        print("Baking Margherita Pizza")

    def box(self):
        print("Boxing Margherita Pizza")

class PepperoniPizza(Pizza):
    def prepare(self):
        print("Preparing Pepperoni Pizza")

    def bake(self):
        print("Baking Pepperoni Pizza")

    def box(self):
        print("Boxing Pepperoni Pizza")
        
        
