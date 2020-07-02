# Binary Tree Level Order Traversal II

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        levels = []
        
        if not root:
            return levels
        
        def helper(node, level):
            if len(levels) == level:
                levels.append([])
            
            levels[level].append(node.val)
            
            if node.left:
                helper(node.left, level + 1)
            
            if node.right:
                helper(node.right, level + 1)
            
        helper(root, 0)
        return levels[::-1]
