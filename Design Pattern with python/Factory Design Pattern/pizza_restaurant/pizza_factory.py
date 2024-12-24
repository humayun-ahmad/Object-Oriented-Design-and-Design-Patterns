from pizza import MargheritaPizza, PepperoniPizza

class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type):
        if pizza_type == "margherita":
            return MargheritaPizza()
        elif pizza_type == "pepperoni":
            return PepperoniPizza()
        else:
            raise ValueError(f"Unknown pizza type: {pizza_type}")
