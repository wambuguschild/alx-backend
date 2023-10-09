#!/usr/bin/env python3
"""LIFO Caching"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class implements a caching system using the LIFO algorithm.

    Attributes:
        MAX_ITEMS (int): The max no. of items that can be stored in the cache.

    Methods:
        __init__(): Initializes an instance of the LIFOCache class.
        put(key, item): Adds an item to the cache using LIFO eviction.
        get(key): Retrieves an item from the cache based on the provided key.
        print_cache(): Prints the current contents of the cache in LIFO order.
    """

    def __init__(self):
        """
        Initializes an instance of the LIFOCache class.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Adds an item to the cache using LIFO eviction.

        Args:
            key (str): The key for the item.
            item (str): The item to be cached.
        """
        # Check if key and item are not None
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # If the cache is full, remove the last item (LIFO eviction)
                last_key = self.order.pop()
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}\n")
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        Retrieves an item from the cache based on the provided key.

        Args:
            key (str): The key to look up in the cache.

        Returns:
            str: The value associated with the key if it exists,
            None otherwise.
        """
        # Check if key is not None and if the key exists in the cache_data
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None

    def print_cache(self):
        """
        Prints the current contents of the cache in LIFO order.
        """
        print("Current cache:")
        for key in self.order:
            # Print the contents of the cache in LIFO order
            print("{}: {}".format(key, self.cache_data.get(key)))
