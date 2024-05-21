#!/usr/bin/python3
"""FIFOCache Module"""
from base_caching import BaseCaching
from queue import Queue


class FIFOCache(BaseCaching):
    """Implements a FIFO cache"""
    def __init__(self):
        """Constructor"""
        self.queue = []
        super().__init__()

    def put(self, key, item):
        """Add an item to cache"""
        if key is None and item is None:
            return

        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first = self.queue.pop(0)
            del self.cache_data[first]

            print("DISCARD:", first)

        # add key to queue
        self.queue.append(key)

    def get(self, key):
        """Gets an item from cache"""
        if key is None or item is None:
            return None

        return self.cache_data.get(key)
