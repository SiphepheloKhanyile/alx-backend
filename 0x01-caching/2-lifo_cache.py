#!/usr/bin/env python3
"""
`FIFOCache` module that inherits from `BaseCaching`
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """
        Initialization
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assigns `item` to caching dictionary using `key`
        Args:
            key : Dictionary Key
            item : Value
        """
        if (key is None or item is None):
            return

        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """
        Returns `key` value in cache ditcionary
        Args:
            key : Value key
        """
        if (key is None or self.cache_data.get(key) is None):
            return None

        return self.cache_data.get(key)
