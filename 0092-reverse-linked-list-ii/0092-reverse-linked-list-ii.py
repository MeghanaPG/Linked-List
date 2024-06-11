# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Time Complexity:
        dummy = ListNode(0, head)

        # 1)reach node at position left 
        leftPrev, cur = dummy, head
        for i in range(left-1):
            leftPrev, cur = cur, cur.next

        # now cur="left" and leftPrev = "node before left"
        # 2) reverse from left to right 
        # we basically reverse the link
        prev = None 
        for i in range(right - left + 1):
            tmpNext = cur.next 
            cur.next = prev 
            prev, cur = cur, tmpNext 

        # 3) Update the pointers
        # 2 should point to last node 
        #cur is the node after right
        leftPrev.next.next = cur 
        leftPrev.next = prev #prev is right
        return dummy.next 

