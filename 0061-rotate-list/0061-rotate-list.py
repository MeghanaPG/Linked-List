# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # time complexity: O(n)
        # count backwards, (length - k - 1)
        if not head:
            return head 

        # get length
        length, tail = 1, head 
        while tail.next:
            tail = tail.next 
            length += 1 
        
        k = k % length 
        if k == 0:
            return head 
        
        # Move to the pivot and start the rotate 
        cur = head 
        for i in range(length - k - 1):
            cur = cur.next 
        newHead = cur.next
        cur.next = None 
        tail.next = head 
        return newHead



