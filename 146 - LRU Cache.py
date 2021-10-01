from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.size=capacity
        self.ca = OrderedDict()
    def get(self, key: int) -> int:
        if key not in self.ca.keys():
            return -1
        self.ca.move_to_end(key)
        return self.ca[key]
    def put(self, key: int, value: int) -> None:
        if key in self.ca.keys():
            self.ca[key]=value
            self.ca.move_to_end(key)
        else:
            self.ca[key]=value
        if len(self.ca)>self.size:
            self.ca.popitem(0)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)