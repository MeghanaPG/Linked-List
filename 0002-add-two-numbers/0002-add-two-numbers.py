# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        reversed_l1 = 0
        reversed_l2 = 0
        carry = 0  # Variable to track the carry when adding digits

        # Initialize a dummy head node for the result linked list.
        head = ListNode()
        current = head

        # Calculate the sum of the two linked lists and store it in reversed order.
        while l1 or l2 or carry:
            if l1:
                reversed_l1 += l1.val
                l1 = l1.next
            if l2:
                reversed_l2 += l2.val
                l2 = l2.next

            # Add the carry from the previous step.
            reversed_l1 += carry

            # Calculate the current digit and the carry for the next step.
            digit = (reversed_l1 + reversed_l2) % 10
            carry = (reversed_l1 + reversed_l2) // 10

            # Create a new node for the result linked list.
            current.next = ListNode(digit)
            current = current.next

            # Reset the reversed values for the next iteration.
            reversed_l1 = 0
            reversed_l2 = 0

        return head.next  # Skip the dummy head node and return the actual result.

    