

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        nodeSeen = []
        
        while head is not None:
            # If node is already present, return True
            if head in nodeSeen:
                return True
            else:
                # If node has not been seen before, add it to the list
                nodeSeen.append(head)
            
            head = head.next
            
        return False
