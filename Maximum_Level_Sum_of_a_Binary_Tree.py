# Maximum Level Sum of a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return
        levels = []
        
        def helper(node, level):
            if len(levels) == level:
                levels.append([])
            
            levels[level].append(node.val)
            
            if node.left:
                helper(node.left, level + 1)
            
            if node.right:
                helper(node.right, level + 1)
        
        helper(root, 0)
        
        idx = float('-inf')
        s = float('-inf')
        
        for i, num in enumerate(levels):
            if sum(num) > s:
                idx = i
            s = max(s, sum(num))
        
        return idx + 1
