# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy 

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next 

            # reverse group 
            prev, curr = kth.next, groupPrev.next 

            # while curr does not reach the end 
            while curr != groupNext:
                temp = curr.next 
                curr.next = prev
                prev = curr
                curr = temp 

            # This part is about placing the group according to the problem 
            # initially this is the first node
            temp = groupPrev.next 
            # putting kth at the beginning of our group 
            groupPrev.next = kth 
            groupPrev = temp
        return dummy.next
     
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next 
            k -= 1 
        return curr
        