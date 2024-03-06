# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
         # Two Pointers 
        # Time Complexity: O(n)
        dummy = ListNode(0, head)
        left = dummy 
        right = head 

        # we keep shifting till n=0, it means we have shifted 
        # keeping the gap between left and right of "n" ->offset of n
        # first we move just the right pointer and then we do both left and right pointers
        while n>0 and right:
            right = right.next 
            n -= 1 
        
        while right:
            left = left.next 
            right = right.next 

        # delete operation 
        left.next = left.next.next 
        return dummy.next 
        