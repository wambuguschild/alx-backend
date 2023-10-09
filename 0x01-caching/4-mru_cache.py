#!/usr/bin/env python3
"""MRU Caching"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class inherits from BaseCaching and implements
    a caching system using the Most Recently Used (MRU) algorithm.
    """

    def __init__(self):
        """
        Constructor to initialize an instance of MRUCache.
        """
        super().__init__()
        self.access_order = []

    def put(self, key, item):
        """
        Add an item in the cache using the MRU algorithm.

        Args:
            key: The key to be used for caching.
            item: The item to be cached.

        If key or item is None, this method does nothing.
        If the number of items in self.cache_data is higher
        than BaseCaching.MAX_ITEMS,
        the most recently used item (MRU) is discarded,
        and a "DISCARD" message is printed.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                mru_key = self.access_order.pop()
                del self.cache_data[mru_key]
                print(f"DISCARD: {mru_key}\n")
            self.cache_data[key] = item
            self.access_order.insert(0, key)

    def get(self, key):
        """
        Get an item by key from the cache.

        Args:
            key: The key to look up in the cache.

        Returns:
            The value in self.cache_data linked to the given key.
            If key is None or if the key doesn’t exist
            in self.cache_data, returns None.

        The accessed key is moved to the front
        of the access order list (most recently used).
        """
        if key is not None and key in self.cache_data:
            self.access_order.remove(key)
            self.access_order.insert(0, key)
            return self.cache_data[key]
        else:
            return None
