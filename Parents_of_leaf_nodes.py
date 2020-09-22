# Program to print the parents of all leaf nodes in a Binary Search Tree

from collections import deque

# Tree Node definition
class TreeNode:
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None

# Check if the node is a leaf node
def isLeafNode(node):
  return node.left is None and node.right is None

# Inorder Traversal for the Leaf Nodes
def printPathIterative(leafnode, d):
  res = []
  count = 0
  curr = leafnode

  while d[curr]:
    count += 1
    if count == 2:
      res.append(curr.val)
      count = 0
    print(curr.val, end=" -> ")
    curr = d[curr]
  print(curr.val)
  return res

# Find and return Parents of the leaf nodes
def printParent(root):
  stack = deque()
  d = {}
  d[root] = None
  stack.append(root)
  parents = []

  while stack:
    curr = stack.pop()

    if isLeafNode(curr):
      parents.append(printPathIterative(curr, d))
    
    if curr.right:
      stack.append(curr.right)
      d[curr.right] = curr
    
    if curr.left:
      stack.append(curr.left)
      d[curr.left] = curr
  
  ans = [parents[i][0] for i in range(len(parents))]
  return set(ans)


# Test
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.left.left = TreeNode(8)
root.right.left.right = TreeNode(9)

print("Parents of all Leaf Nodes: ", printParent(root))
