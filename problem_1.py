import collections


class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key=None):
        # Retrieve item from provided key. Return -1 if nonexistent.
        try:
            if key == None:
                return "Key can't be empty"
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1

    def set(self, key, value=None):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if value is None:
            print("Value can't be empty")
            return
        else:
            try:
                
                self.cache.pop(key)
            except KeyError:
                if len(self.cache) >= self.capacity:
                    self.cache.popitem(last=False)
            self.cache[key] = value


# Case 1
test1 = LRU_Cache(5)

test1.set(1, 1)

print(test1.get(1))       # returns 1
print(test1.get(3))       # return -1

# Case 2
test2 = LRU_Cache(5)
test2.set(1)
print(test2.get(1)) # TypeError

# Case 3
test3 = LRU_Cache(5)
test3.set(1, 1)
print(test3.get()) # TypeError:
