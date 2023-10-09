#!/usr/bin/env python3
"""LIFO Caching"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.order = []  # Initialize the order list

    def put(self, key, item):
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # If the cache is full, remove the last item (LIFO eviction)
                last_key = self.order.pop()
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}\n")
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None

    def print_cache(self):
        print("Current cache:")
        for key in self.order:
            print("{}: {}".format(key, self.cache_data.get(key)))
