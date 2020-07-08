# Increasing Triplet Subsequence

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        minOne = 2**31 - 1
        minTwo = 2**31 - 1
        
        if nums is None or len(nums) < 3:
            return False
        
        for i in range(len(nums)):
            if nums[i] < minOne:
                minOne = nums[i]
            
            if nums[i] > minOne:
                minTwo = min(nums[i], minTwo)
            
            if nums[i] > minTwo:
                return True
        
        return False
