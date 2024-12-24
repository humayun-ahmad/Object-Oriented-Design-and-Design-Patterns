from coffee import CoffeeDecorator

class MilkDecorator(CoffeeDecorator):
    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.5

    def get_description(self) -> str:
        return self._coffee.get_description() + ", milk"

class SugarDecorator(CoffeeDecorator):
    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.2

    def get_description(self) -> str:
        return self._coffee.get_description() + ", sugar"

class WhippedCreamDecorator(CoffeeDecorator):
    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.7

    def get_description(self) -> str:
        return self._coffee.get_description() + ", whipped cream"