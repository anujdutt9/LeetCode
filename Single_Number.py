# Single Number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Get the 1st element
        a = nums[0]
        
        # Apply XOR Operation with rest of the elements
        for i in range(1, len(nums)):
            a ^=nums[i]
        return a
        
