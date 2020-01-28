# Intersection of Two Arrays
# https://leetcode.com/problems/intersection-of-two-arrays/

# Time Complexity: O(n x m)
# Using Numpy
import numpy as np

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return np.intersect1d(np.sort(nums1), np.sort(nums2))

# Using Python's built-in intersection facilities
# Time Complexity: O(n x m)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1)