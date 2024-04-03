#!/usr/bin/env python3
"""Task 0 Module"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Defines a class for caching information in key-value pairs
    Methods:
        put(key, item) - store a key-value pair
        get(key) - retrieve the value associated with a key
    """
    def __init__(self):
        """
        Initialize the class using the parent class __init__ method
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        '''
        store a key/value pair to the cache
        '''
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        '''
        return value in self.cache_data linked to key
        '''
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
