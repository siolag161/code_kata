
from discount import DefaultDiscount, FreeComplimentariesDiscount

class Cart(object):
    def __init__(self, items, *args, **kwargs):
        self.items = items
        self.promotions = [DefaultDiscount]

    def calc_discounts(self, *args, **kwargs):
        return sum(discount.calc(self, *args, **kwargs) for discount in self.promotions)

    def apply_promotion(self, promotion):
        self.promotions.append(promotion)

    def calc_total(self):
        supposed_val =  self.items.calc_total_price()
        return supposed_val
