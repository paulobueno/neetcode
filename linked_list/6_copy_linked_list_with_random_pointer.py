# URL https://neetcode.io/problems/copy-linked-list-with-random-pointer
# Time Complexity: O(n)
# Space Complexity: O(n)


from typing import List

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy_map = {}

        curr_node = head
        while curr_node:
            copy_map[curr_node] = Node(curr_node.val)
            curr_node = curr_node.next

        curr_node = head
        while curr_node:
            copy_map[curr_node].next = copy_map[curr_node.next] if curr_node.next else None
            copy_map[curr_node].random = copy_map[curr_node.random] if curr_node.random else None
            curr_node = curr_node.next

        return copy_map[head] if head else None

