# URL https://neetcode.io/problems/reverse-a-linked-list
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return head

        curr_node = head
        new_next = None
        while curr_node is not None:
            old_next = curr_node.next
            curr_node.next = new_next
            new_next = curr_node
            curr_node = old_next

        return new_next


