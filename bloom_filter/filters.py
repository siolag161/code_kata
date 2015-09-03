
"""
"""
from bitarray import bitarray
import mmh3

class MurmurHash(object):
    def __init__(self, m=25, seed=0):
        self.m = m
        self.seed = seed

    def __call__(self, value):
        return mmh3.hash(value, self.seed) % self.m

class BloomFilter(object):
    """
    """

    def __init__(self, m=25, k=3):
        self.m = m
        self.k = k
        self.hash_funcs = self._init_hash_functions(m, k)
        self.vector = bitarray(m)

    @classmethod
    def _init_hash_functions(cls, m, k):
        return [MurmurHash(m, i) for i in xrange(k)]

    def hash(self, value):
        return (hash_func(value) for hash_func in self.hash_funcs)

    def check_value(self, value):
        return all(self.vector[val] == 1 for val in self.hash(value))

    def set_value(self, value):
        for val in self.hash(value):
            self.vector[val] = 1


