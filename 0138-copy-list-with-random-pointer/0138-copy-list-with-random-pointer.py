"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #Time Complexity: O(n)
        #Two passes and we are creating the HashMap 
        oldToCopy = {None:None}

        cur = head 
        while cur:
            # new node with cur.val
            copy = Node(cur.val)
            # we are using the hashmap and copying the old node to the copy node 
            oldToCopy[cur] = copy 
            cur = cur.next 

        cur = head 
        # In this part we will be allocating the ptrs to the copy we created 
        while cur:
            # getting ther copy node of the current node 
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next 
        return oldToCopy[head]
            
