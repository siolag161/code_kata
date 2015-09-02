import unittest

from .product import (Product, ProductItem, ProductItemSet)
from .cart import (Cart, FreeComplimentariesDiscount)

class TestProducts(unittest.TestCase):
    def test_create_product(self):
        p = Product(name="car")
        self.assertEqual(p.name, "car")
        self.assertEqual(p.calc_unit_price(), 0.0)

    def test_create_product_with_price(self):
        p = Product(name="shirt", unit_price = 1.0)
        self.assertEqual(p.calc_unit_price(), 1.0)
        self.assertEqual(p.name, "shirt")

class TestItemPricing(unittest.TestCase):
    def setUp(self):
        self.product = Product(name="shirt", unit_price = 24.0)

    def test_create_item(self):
        item = ProductItem(product = self.product)
        self.assertEqual(item.quantity(), 0.0)

        item.qty = 10
        self.assertEqual(item.calc_total_price(), 240.0)

class TestCarts(unittest.TestCase):
    def setUp(self):
        self.shirt = Product(name="shirt", unit_price = 24.0)
        self.dvd = Product(name="dvd", unit_price = 16.0)

        self.shirt_item = ProductItem(self.shirt, quantity = 10)
        self.dvd_item = ProductItem(self.dvd, quantity = 15)

        self.items = ProductItemSet()
        self.items.add_item(self.shirt_item)
        self.items.add_item(self.dvd_item)

        self.cart = Cart(items = self.items)

    def test_prices(self):
        self.assertEqual(self.cart.calc_total(), 480)

    def test_buy_2_get_1_free(self):
        b2g1f_discount = FreeComplimentariesDiscount(product=self.shirt, m=2, n=1)
        self.cart.apply_promotion(b2g1f_discount)

        new_value = self.cart.calc_total()
        self.assertEqual(new_value, 480.0)
        discount_value = b2g1f_discount.calc(self.cart)
        self.assertEqual(discount_value, 72.0) # 3 free complementaries

    def test_buy_2_get_1_free_for_2_articles(self):
        self.items = ProductItemSet()
        self.cart = Cart(items = self.items)
        self.items.add_item(ProductItem(self.shirt, quantity = 2))

        b2g1f_discount = FreeComplimentariesDiscount(product=self.shirt, m=2, n=1)
        self.cart.apply_promotion(b2g1f_discount)
        new_value = self.cart.calc_total()
        self.assertEqual(new_value, 48.0)
        discount_value = b2g1f_discount.calc(self.cart)
        self.assertEqual(discount_value, 0.0) # 0 free complementaries

    def test_buy_2_get_1_free_for_3_articles(self):
        self.items = ProductItemSet()
        self.cart = Cart(items = self.items)
        self.items.add_item(ProductItem(self.shirt, quantity = 3))
        new_value = self.cart.calc_total()
        self.assertEqual(new_value, 72.0)

        b2g1f_discount = FreeComplimentariesDiscount(product=self.shirt, m=2, n=1)
        self.cart.apply_promotion(b2g1f_discount)

        discount_value = b2g1f_discount.calc(self.cart)
        self.assertEqual(discount_value, 24.0) # 1 free complementaries
