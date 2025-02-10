# URL https://neetcode.io/problems/remove-node-from-end-of-linked-list
# Time Complexity: O(x)
# Space Complexity: O(x)

from typing import List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: 
        qty_nodes = 0
        curr_node = head
        while curr_node:
            qty_nodes += 1
            curr_node = curr_node.next

        n = qty_nodes - n

        if n == 0:
            return head.next
        
        curr_node_position = 0
        curr_node = head
        while curr_node_position < n:
            prev = curr_node
            curr_node = curr_node.next
            if curr_node is None:
                curr_node = head
            curr_node_position += 1

        prev.next = curr_node.next

        return head
