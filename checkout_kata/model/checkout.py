"""
Checkout Class to calculate total price of all items in basket

For Test Purpose, classes are defined with limited implementations.

"""
import logging
import abc


logger = logging.getLogger()

# Product Class for items, unit price, stock quantity etc.,
class Product(abc.ABC):
    """Product Class
    """
    def __init__(self, unit_price):
        logger.info("Product class is called.")
        self.unit_price = unit_price
        
    @abc.abstractmethod
    def get_price(self, quantity):
        pass
        
    @property    
    def get_unit_price(self, item):
        """Method to get unit price of Item
        """
        if item in self.products['item']:
            price = self.products['unit_price']
            return price
    
class SinglePricedProduct(Product):
    """SubClass of Product 
        - to get single item price
    """
    def get_price(self, quantity):
        """Method to get single item price
        """
        return self.unit_price * quantity

class MultiPricedProduct(Product):
    """SubClass of Product 
        - to get Special item price
    """
    def __init__(self, unit_price, special_price, special_quantity):
        super().__init__(unit_price)
        self.special_price = special_price
        self.special_quantity = special_quantity

    def get_price(self, quantity):
        """Method to get special price for multiple items
        """
        normal_price = quantity % self.special_quantity * self.unit_price
        special_price = quantity // self.special_quantity * self.special_price
        return normal_price + special_price
    
    
# Checkout Class for adding items into cart and calculating total price
class Checkout:
    """Checkout class
    """
    logger.info("Checkout Class is called")
    
    def __init__(self, products):
        """Initializing checkout class with empty basket
        """
        self.products = products
        self.basket = {}
        
    def add_item(self, item, qty):
        """Method should add item into basket
        """
        # if item in basket it will count 
        if item in self.products:
            if item in self.basket:
                self.basket[item] += qty
            else:
                self.basket[item] = qty
                
    def total_price(self):
        """Method to calculate total price
        """
        total = 0
        for product_code, quantity in self.basket.items():
            total += self.products[product_code].get_price(quantity)
        return total
        
 
 
if __name__ == "__main__":       
    # Define Product
    products = {
        "A": MultiPricedProduct(50, 130, 3),
        "B": MultiPricedProduct(30, 45, 2),
        "C": SinglePricedProduct(10)
    }
    # Creating Checkout Object
    checkout = Checkout(products)
    
    # Testing Purpose
    # Adding items
    add_A = checkout.add_item("A", 4)
    add_B = checkout.add_item("B", 5)
    add_c = checkout.add_item("C", 2)
    
    # Calculating total price
    total = checkout.total_price()
    print(f"Total Price of Added Items: GBP {total}/-")    # Printing out the total price
    