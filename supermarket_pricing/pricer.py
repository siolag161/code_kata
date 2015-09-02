
__all__ = [ 'DefaultPricer' ]

def pricer_strategy(f):
    class Pricer(object):
        def __repr__(self):
            return f.__name__
        def __call__(self, product, *args, **kwargs):
            return f(product, *args, **kwargs)
    Pricer.price = Pricer.__call__
    Pricer.__name__ = f.__name__
    return Pricer()

@pricer_strategy
def DefaultPricer(item, *args, **kwargs):
    return item.product.calc_unit_price()*item.quantity()
