# URL https://neetcode.io/problems/reorder-linked-list


from typing import List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        node = head
        while node:
            nodes.append(node)
            node = node.next

        l, r = 0, len(nodes) - 1
        while l < r:
            nodes[l].next = nodes[r]
            l += 1
            if l >= r:
                break
            nodes[r].next = nodes[l]
            r -= 1

        nodes[l].next = None


# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle

        # revert second part

        # merge two parts





