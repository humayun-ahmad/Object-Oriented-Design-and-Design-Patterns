from abc import ABC, abstractmethod

# Interface for Grocery Items
class GroceryItem(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def get_store_name(self):
        pass
