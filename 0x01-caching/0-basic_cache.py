#!/usr/bin/python3
"""BasicCache Module"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Implements a basic cache"""

    def put(self, key, item):
        """Add an item to the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Gets an items from cache"""
        if key is None:
            return None

        return self.cache_data.get(key)
