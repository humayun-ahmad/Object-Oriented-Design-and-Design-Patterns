from item import Item
from grocery_item import GroceryItem

# Adapter for GroceryItem to conform to Item
class GroceryItemAdapter(Item):
    def __init__(self, item: GroceryItem):
        self.item = item

    def get_item_name(self):
        return self.item.get_name()

    def get_price(self):
        return self.item.get_price()

    def get_restaurant_name(self):
        return self.item.get_store_name()
