#!/usr/bin/env python3
"""Create a class BasicCache that inherits from BaseCaching and is a caching
system:

    You must use self.cache_data - dictionary from parent class BaseCaching
    This caching system doesn’t have limit
    def put(self, key, item):
        Assign to dictionary self.cache_data the item value for the key key
        If key or item is None, this method should not do anything.
    def get(self, key):
        Must return the value in self.cache_data linked to key.
        If key is None or doesn’t exist in self.cache_data, return None.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Object allowing storing and retrieving items from a dictionary."""
    def put(self, key, item):
        """Puts an item in the cache."""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key."""
        return self.cache_data.get(key, None)
