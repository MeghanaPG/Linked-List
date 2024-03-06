# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time Complexity: O(n)
        # Iterative solution 
        # prev, curr = None, head 

        # while curr:
        #     # Temporary variable 
        #     nxt = curr.next 
        #     curr.next = prev 
        #     # update the pointers 
        #     prev = curr 
        #     curr = nxt 
        # return prev 
        # Time Complexity: O(n)
        # Recursive solution 
        if not head: 
            return None 

        newHead = head 
        if head.next: 
            newHead = self.reverseList(head.next)
            head.next.next = head 
        head.next = None 

        return newHead 