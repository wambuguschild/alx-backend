#!/usr/bin/env python3
""" FIFOCache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class, a caching system using FIFO algorithm.
    """

    def __init__(self):
        """ Initialize a FIFO cache.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item to the cache_data dictionary using FIFO eviction.
        Args:
            key: The key for the item.
            item: The item to be cached.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # If the cache is full, remove the first item (FIFO eviction)
                removed_key = self.order[0]
                del self.cache_data[removed_key]
                print(f"DISCARD: {removed_key}\n")
                self.order.pop(0)

            # Add the new item to the cache_data and update the order
            self.cache_data[key] = item
            self.order.append(key)

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
