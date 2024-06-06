# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Time Complexity: O(n+m)
        curr = list1
        i = 0 
        # considering the nodes before a and attaching list2 after that 
        while i < a - 1:
            curr = curr.next
            i += 1 
        
        # a = 3, b = 4 
        # 0 1 2 [3 4] 5 6 7 
        # now head point to index 2 as we traversed till a 
        head = curr
        # <= as we need to stop at index 5 
        while i <= b:
            curr = curr.next 
            i += 1 
        head.next = list2 

        while list2.next:
            list2 = list2.next 
        list2.next = curr
        return list1
        

