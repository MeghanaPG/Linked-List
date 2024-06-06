# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Monotonic Decreasing the stack 
        stack = []
        cur = head 

        while cur:
            while stack and cur.val > stack[-1]:
                stack.pop()
            stack.append(cur.val)
            cur = cur.next

        # Now we will convert the stack values into a Linked List 
        dummy = ListNode()
        cur = dummy 
        for n in stack:
            cur.next = ListNode(n)
            cur = cur.next 
        return dummy.next 
