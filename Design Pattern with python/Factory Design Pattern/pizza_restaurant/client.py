from pizza_factory import PizzaFactory
def order_pizza(pizza_type):
    factory = PizzaFactory()
    pizza = factory.create_pizza(pizza_type)  # Factory creates the pizza
    pizza.prepare()
    pizza.bake()
    pizza.box()

# Example usage
order_pizza("margherita")
order_pizza("pepperoni")
