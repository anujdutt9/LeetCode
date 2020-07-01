# Remove Nth node from Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        currNode = prevNode = head
        step = 1
        
        while currNode.next:
            step += 1
            currNode = currNode.next
            
            if step > n + 1:
                prevNode = prevNode.next
        
        if step == n:
            return head.next
        else:
            prevNode.next = prevNode.next.next
            return head
