# Doubly Linked List 
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity 
        self.cache = {} #map key to node 

        # Left = LRU, right = Most recent 
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left 

    # at left we remove, as the left is the least recenlty used 
    def remove(self, node):
        prev, nxt = node.prev, node.next 
        prev.next, nxt.prev = nxt, prev 

    # at right because it is the most recent 
    def insert(self, node):
        prev, nxt = self.right.prev, self.right 
        prev.next = nxt.prev = node 
        node.next, node.prev = nxt, prev 

    def get(self, key: int) -> int:
        if key in self.cache:
            # we remove to get the recent one 
            self.remove(self.cache[key])
            # inserting it again as it is the Most recently used 
            self.insert(self.cache[key])
            return self.cache[key].val 
        return -1 
        
    # put method is to update or modify an existing resource 
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from list and delete the LRU from the hashmap 
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)