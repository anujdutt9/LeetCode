# Reverse Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prevNode = None
        currNode = head
        
        while currNode is not None:
            tmp = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = tmp
        
        return prevNode
