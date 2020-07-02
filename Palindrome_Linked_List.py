# Palindrome Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        a = []
        
        currNode = head
        
        while currNode is not None:
            a.append(currNode.val)
            currNode = currNode.next
        
        return a == a[::-1]
        
