#!/usr/bin/env python3
"""Create MRUCache class that inherits from BaseCaching and is a caching
system:

    You must use self.cache_data - dictionary from parent class BaseCaching
    You can overload def __init__(self): but don’t forget to call the parent
    init: super().__init__()
    def put(self, key, item):
        Assign to dictionary self.cache_data the item value for the key key.
        If key or item is None, this method should not do anything.
        If number of items in self.cache_data is higher than
        BaseCaching.MAX_ITEMS:
            you must discard the first item put in cache (MRU algorithm)
            you must print DISCARD: with the key discarded followed by a new
            line def get(self, key):
        Must return the value in self.cache_data linked to key.
        If key is None or if doesn’t exist in self.cache_data, return None.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """An object that allows storing and retrieving items from a dictionaryt"""
    def __init__(self):
        """Initializes the cache."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache."""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                mru_key, _ = self.cache_data.popitem(False)
                print("DISCARD:", mru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key."""
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
