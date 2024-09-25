# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head 
        tail = dummy = ListNode()
        
        # 0 1 2 3 0 4 5 0 6 7 8 0
        while cur.next:
            node = ListNode(0)
            while cur.next.val != 0:
                node.val += cur.next.val
                cur = cur.next 
            tail.next = node 
            tail = tail.next
            cur = cur.next 

        return dummy.next 
