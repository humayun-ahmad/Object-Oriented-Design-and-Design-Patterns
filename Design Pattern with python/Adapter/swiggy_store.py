from item import Item

# SwiggyStore to manage items
class SwiggyStore:
    def __init__(self):
        self.items = []

    def add_items(self, item: Item):
        self.items.append(item)

    def show_items(self):
        for item in self.items:
            print(f"Item Name: {item.get_item_name()}")
            print(f"Price: {item.get_price()}")
            print(f"Restaurant/Store Name: {item.get_restaurant_name()}")
            print("-" * 30)
