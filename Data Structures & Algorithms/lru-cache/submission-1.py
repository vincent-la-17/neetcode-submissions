class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache.keys():
            self.cache.move_to_end(key, last = True)
        return self.cache.get(key, -1)     
       

    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            self.cache.move_to_end(key, last = True)
        self.cache[key] = value
        while len(self.cache) > self.cap:
            self.cache.popitem(last=False)

