# Cache

## Cache Replacement Policies: `FIFO`, `LIFO`, `LRU`,`MRU`, `LFU`

## Requirements
* Code should use the `pycodestyle` (version 2.5)
* All files must be executable
* All modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
   
## More Info:
* Parent class `BaseCaching`
* All classes must inherit from `BaseCaching` defined below:
    ```
    #!/usr/bin/python3
    """ BaseCaching module"""

    class BaseCaching():
        """ BaseCaching defines:
          - constants of your caching system
          - where your data are stored (in a dictionary)
        """
        MAX_ITEMS = 4

        def __init__(self):
            """ Initiliaze"""
            self.cache_data = {}

        def print_cache(self):
            """ Print the cache"""
            print("Current cache:")
            for key in sorted(self.cache_data.keys()):
                print("{}: {}".format(key, self.cache_data.get(key)))

        def put(self, key, item):
            """ Add an item in the cache"""
            raise NotImplementedError("put must be implemented in your cache class")

        def get(self, key):
            """ Get an item by key"""
            raise NotImplementedError("get must be implemented in your cache class")
    ```
