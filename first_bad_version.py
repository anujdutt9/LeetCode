# First Bad Version
# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Applying Binary Search
        left = 1
        right = n

        while (left < right):
            # Middle Value Index
            mid = (left + right) / 2
            if (isBadVersion(mid)):
                right = mid
            else:
                left = mid + 1
        return int(left)