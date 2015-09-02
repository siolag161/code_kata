
"""
"""

from .pricer import DefaultPricer

class Product(object):
    def __init__(self, name, *args, **kwargs):
        "docstring"
        self.name = name
        self.unit_price = kwargs.get('unit_price', 0.0)

    def calc_unit_price(self,):
        return self.unit_price


class ProductItem(object):
    """item for one single product"""
    def __init__(self, product, quantity = 0.0, pricer = DefaultPricer, *args, **kwargs):
        self.product = product
        self.qty = quantity
        self.pricer = pricer

    def quantity(self,):
        return self.qty

    def add_items(self, qty):
        self.qty += qty

    def remove_items(self, qty):
        self.qty -= qty

    def calc_total_price(self,):
        return self.pricer.price(self) if self.pricer else self.product.calc_unit_price()*self.quantity()

    def __str__(self):
        return "item: %s with stock: %s" %(self.product.name, self.qty)

class ProductItemSet(ProductItem):
    """set of prducts"""
    def __init__(self, pricer = DefaultPricer, *args, **kwargs):
        self.pricer = pricer
        self.items = {}

    def quantity(self,):
        return (item.quantity() for item in self)

    def get_product(self, product_name):
        return self.items.get(product_name, None)

    def get_product_quantity(self, product_name):
        return self.get_product(product_name).quantity()

    def calc_prices(self):
        return (item.calc_total_price() for item in self)

    def add_item(self, item):
        current_item = self.items.get(item.product.name, None)
        if current_item:
            current_item.add_item(item.quantity())
        else:
            self.items[item.product.name] = ProductItem(product=item.product, quantity=item.qty, pricer=item.pricer)

    def __iter__(self,):
        return self.items.itervalues() # iterate over values (product item)

    def calc_total_price(self,):
        return sum(self.calc_prices())
