# Remove Duplicates from Sorted Array in-place

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        l = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[l] = nums[i]
                l += 1
        return l
               
