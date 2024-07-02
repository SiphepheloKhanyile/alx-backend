#!/usr/bin/env python3
"""
Inherits from BaseCaching Class
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Inherits from BaseCaching and is a caching system
    """

    def put(self, key, item):
        """
        Assigns `item` to caching dictionary using `key`
        Args:
            key : Dictionary Key
            item : Value
        """
        if (key is None or item is None):
            return

        self.cache_data[key] = item

    def get(self, key):
        """
        Returns `key` value n cache ditcionary
        Args:
            key : Value key
        """
        if (key is None or self.cache_data.get(key) is None):
            return None

        return self.cache_data.get(key)
