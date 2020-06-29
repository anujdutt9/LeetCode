# Remove Duplicates from Sorted Array in-place

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        # Keep track of Array Length
        l = 1
        
        # Since, we want to get the length in-place i.e.
        # without using any extra memory
        for i in range(1, len(nums)):
            # If the elements are not same
            if nums[i] != nums[i-1]:
                # overwrite the element at index
                nums[l] = nums[i]
                # Increment the Length
                l += 1
        return l
