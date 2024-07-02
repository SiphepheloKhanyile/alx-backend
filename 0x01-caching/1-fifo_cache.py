#!/usr/bin/env python3
"""
`FIFOCache` module that inherits from `BaseCaching`
"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
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

        # items_length = len(self.cache_data) + 1

        # self.cache_data[key] = item

        # if items_length > BaseCaching.MAX_ITEMS:
        #     keys = list(self.cache_data.keys())
        #     print(f"DISCARD: {keys[0]}")
        #     del self.cache_data[keys[0]]
        #     self.cache_data[key] = item

        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """
        Returns `key` value in cache ditcionary
        Args:
            key : Value key
        """
        if (key is None or self.cache_data.get(key) is None):
            return None

        return self.cache_data.get(key)
