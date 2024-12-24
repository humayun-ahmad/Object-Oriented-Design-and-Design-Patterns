from swiggy_store import SwiggyStore
from food_item import FoodItem
from grocery_item_adapter import GroceryItemAdapter
from grocery_product import GroceryProduct

# Main function to demonstrate the pattern
def main():
    swiggy_store = SwiggyStore()
    swiggy_store.add_items(FoodItem())
    swiggy_store.add_items(FoodItem())
    # Adapter for GroceryItem
    swiggy_store.add_items(GroceryItemAdapter(GroceryProduct()))

    swiggy_store.show_items()

if __name__ == "__main__":
    main()
