"""
Author: Puviyarasan Rajininivetha
version: 1.0.1

Test Cases for Checkout Class 

Create a checkout class to calculate total price of items in basket
    - Valid Product must be added into the basket with total qty
    - Total price must be calculated based on the qty and unit price
    - If qty is eligible for special price total price should be calculated accordingly
"""

from unittest import TestCase
import json
from model.checkout import Checkout, MultiPricedProduct, SinglePricedProduct, Product

# Global variable to load data
PRODUCT_DATA = {}

class TestProductModel(TestCase):
    """Test Product class
    """
    def setUp(self):
        """Setup Product class before each test
        """
        global PRODUCT_DATA
        with open("tests/fixtures/product_data.json", "r") as product:
            PRODUCT_DATA = json.load(product)

        
    def tearDown(self):
        """teardown Product class after each test
        """
        self.product = None
        
    ######################################################################
    # T E S T   C A S E S  #  P R O D U C T  #
    ######################################################################    
        
        
    def test_get_price(self):
        """Test single unit price of a Product
        """
        s_pr = PRODUCT_DATA[0]["unit_price"]        
        s_price = SinglePricedProduct(s_pr)
        self.assertEqual(s_price.get_price(1), 50)
        
    def test_multi_price(self):
        """Test special price of items
        """
        u_price = PRODUCT_DATA[0]["unit_price"]
        s_price = PRODUCT_DATA[0]["spl_price"]
        s_qty = PRODUCT_DATA[0]["spl_qty"]
        m_price = MultiPricedProduct(s_price, s_price, s_qty)
        self.assertEqual(m_price.get_price(3), 130)
        
        
class TestCheckoutModel(TestCase):
    """ Test Checkout Model """
    
    def setUp(self):
        """Setup before each test
        """
        global PRODUCT_DATA
        with open("tests/fixtures/product_data.json", "r") as product:
            PRODUCT_DATA = json.load(product)
        self.checkout = Checkout(PRODUCT_DATA)
       
        
    def tearDown(self):
        """TearDown after each test
        """
        self.checkout = None
        
    
    ######################################################################
    # T E S T   C A S E S  #  C H E C K O U T  #
    ######################################################################
    
    def test_to_add_basket(self):
        """Test to add items into basket
        """
        a_item = self.checkout.add_item("A", 3)
        b_item = self.checkout.add_item("B", 4)
        
        # test by checking length
        if a_item in self.checkout.basket:
            self.assertEqual(len(self.checkout.basket), 1)
        
        # test by implementing dict comprehension
        if b_item in self.checkout.basket:
            self.assertEqual(str(self.checkout.basket), {a:b for a, b in self.checkout.basket.items()})
        
            
    def test_checkout(self):
        """Test Checkout the basket with added items and calculate price
        """
        t = self.checkout.total_price()
        a = self.checkout.add_item("A", 3)
        
        # Simple condition checking test 
        if a in self.checkout.basket:
            self.assertEqual(t, 130)