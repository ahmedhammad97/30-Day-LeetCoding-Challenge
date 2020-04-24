from collections import OrderedDict

class LRUCache(object):
    def __init__(self, capacity):
        self.dict = OrderedDict()
        self.capacity = capacity
        

    def get(self, key):
        if key not in self.dict:
            return -1
        self.dict.move_to_end(key, last=True)
        return self.dict[key]
        

    def put(self, key, value):
        if key in self.dict:
            self.dict.move_to_end(key, last=True)
        else:
            if len(self.dict) == self.capacity:
                self.dict.popitem(last=False)
        self.dict[key] = value
        

# Python has a cool data structure `OrderedDict`
# that can be used to easily simulate LRU cache.