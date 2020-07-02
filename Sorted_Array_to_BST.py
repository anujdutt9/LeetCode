# Sorted Array to Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        
        # Get the Middle Value in the Array
        mid = (len(nums)) // 2
        
        # Make it the Root Node
        root = TreeNode(nums[mid])
        
        # Recusively find the mid for the left half of array
        root.left = self.sortedArrayToBST(nums[:mid])
        
        # Recusively find the mid for the right half of array
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        # Return the Root Node for the Tree
        return root
