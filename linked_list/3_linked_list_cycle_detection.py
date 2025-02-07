# URL https://neetcode.io/problems/linked-list-cycle-detection
# Time Complexity: O(n)
# Space Complexity: O(n)
# NOTE: There is a solution with space complexity O(1)


from typing import List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        return False
