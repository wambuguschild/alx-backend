#!/usr/bin/env python3
""" BasicCache module
"""
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """ BasicCache class, a caching system without a limit.
    """

    def put(self, key, item):
        """ Add an item to the cache_data dictionary.
        Args:
            key: The key for the item.
            item: The item to be cached.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache_data dictionary.
        Args:
            key: The key to look up in the cache.
        Returns:
            The value associated with the key if it exists, None otherwise.
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
