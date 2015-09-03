import unittest

from .filters import (MurmurHash, BloomFilter)

class TestCheckContains(unittest.TestCase):
    def test_set_value(self):
        filter = BloomFilter()
        s1 = "string1"
        filter.set_value(s1)

    def test_check_value(self):
        filter = BloomFilter()
        s1 = "string1"
        filter.set_value(s1)
        self.assertTrue(filter.check_value(s1))
        s2 = "string2"
        filter.set_value(s2)
        self.assertTrue(filter.check_value(s2))
        s3 = "string3"
        self.assertFalse(filter.check_value(s3))
