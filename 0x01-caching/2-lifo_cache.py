#!/usr/bin/python3
"""LIFOCache Module"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """Implements a LIFO cache"""
    def __init__(self):
        """Constructor"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to cache"""
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem()
                print("DISCARD:", last_key)

        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Gets an item from cache"""
        return self.cache_data.get(key, None)
