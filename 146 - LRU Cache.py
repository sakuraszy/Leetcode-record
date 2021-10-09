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


##using double linked List
class dlnode():
    def __init__(self,key=None,value=None,next=None,pre=None):
        self.key=key
        self.value=value
        self.next=next
        self.pre=pre
class LRUCache:
    def __init__(self, capacity: int):
        self.size=0
        self.cache={}
        self.capacity=capacity
        self.head=dlnode()
        self.tail=dlnode()
        #initial the double linked list
        self.head.next=self.tail
        self.tail.pre=self.head
    def move_to_head(self,node):
        #remove node from list
        pre=node.pre
        nex=node.next
        pre.next=nex
        nex.pre=pre
        #replace it at head
        node.pre=self.head
        node.next=self.head.next
        self.head.next.pre=node
        self.head.next=node
    def add_node(self,node):
        node.pre=self.head
        node.next=self.head.next
        self.head.next.pre=node
        self.head.next=node
    def remove_last(self):
        removed=self.tail.pre
        if self.size==0:
            return removed
        else:
            self.tail.pre=removed.pre
            removed.pre.next=self.tail
            return removed
    def get(self, key: int) -> int:
        ##return value
        result =self.cache.get(key,None)
        if result != None:
            #move the node to the first
            self.move_to_head(result)
            return result.value
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        node=self.cache.get(key,None)
        if node != None:
            #print(node)
            self.move_to_head(node)
            node.value=value
        else:
            self.size+=1
            newnode= dlnode(key,value)
            self.add_node(newnode)
            self.cache[key]=newnode
            if self.size>self.capacity:
                #remove the last
                removed=self.remove_last()
                self.size-=1
                del self.cache[removed.key]
                
                


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)