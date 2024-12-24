from item import Item

# Implementation of FoodItem
class FoodItem(Item):
    def get_item_name(self):
        return "Food Item"

    def get_price(self):
        return "10 USD"

    def get_restaurant_name(self):
        return "Best Restaurant"
