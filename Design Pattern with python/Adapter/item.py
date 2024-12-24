from abc import ABC, abstractmethod

# Interface for Items
class Item(ABC):
    @abstractmethod
    def get_item_name(self):
        pass

    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def get_restaurant_name(self):
        pass
