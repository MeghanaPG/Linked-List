class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
    # Time complexity: O(n)
        if not head or not head.next:
            return 0
        
        # Store the values of nodes in the linked list in an array
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        
        # Initialize two pointers
        left = 0
        right = len(values) - 1
        
        # Initialize the maximum twin sum
        max_sum = float('-inf')
        
        # Iterate through the array using two pointers
        while left < right:
            twin_sum = values[left] + values[right]  # Calculate the twin sum
            max_sum = max(max_sum, twin_sum)  # Update the maximum twin sum
            left += 1
            right -= 1
        
        return max_sum

