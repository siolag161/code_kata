

__all__ = [ 'DefaultDiscount', 'FreeComplimentariesDiscount' ]


class DefaultDiscount(object):
    def __init__(self, *args, **kwargs):
        pass

    def calc(self, cart, *args, **kwargs):
        return 0.0

class FreeComplimentariesDiscount(DefaultDiscount):
    def __init__(self, *args, **kwargs):
        self.product = kwargs.get("product")
        self.n_base = kwargs.get("m", 1)
        self.n_comp = kwargs.get("n", 0)

    def calc(self, cart, *args, **kwargs):
        self.relevant_items = cart.items.get_product(self.product.name)
        off_base = self.relevant_items.quantity() // (self.n_base + self.n_comp)
        off = off_base * self.product.calc_unit_price()
        return off
