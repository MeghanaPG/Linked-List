class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Time complexity: O(nlogn) -> Binary Search + for each candidate we 
        # iterate over the entire array which takes O(n) time, resulting i a total of O(nlogn) time 
        # if the range is not [1,n] then the value of low and high can be low=0 and high= max(nums). Depending on the condition 
        low = 1
        high = len(nums) - 1 

        while low <= high:
            cur = (low + high) // 2
            count = 0 

            # Count how many numbers are less than or equal to "cur"
            count = sum(num<= cur for num in nums)

            if count > cur:
                duplicate = cur 
                high = cur - 1
            else:
                low = cur + 1 
        return duplicate 
    