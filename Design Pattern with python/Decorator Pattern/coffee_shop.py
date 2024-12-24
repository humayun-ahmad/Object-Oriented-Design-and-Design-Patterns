from coffee import PlainCoffee
from coffee_decorator import MilkDecorator, SugarDecorator, WhippedCreamDecorator

if __name__ == "__main__":

    my_coffee = PlainCoffee()
    print(f"{my_coffee.get_description()} - ${my_coffee.get_cost():.2f}")

    # Add milk
    my_coffee = MilkDecorator(my_coffee)
    print(f"{my_coffee.get_description()} - ${my_coffee.get_cost():.2f}")

    # Add sugar
    my_coffee = SugarDecorator(my_coffee)
    print(f"{my_coffee.get_description()} - ${my_coffee.get_cost():.2f}")

    # Add whipped cream
    my_coffee = WhippedCreamDecorator(my_coffee)
    print(f"{my_coffee.get_description()} - ${my_coffee.get_cost():.2f}")
