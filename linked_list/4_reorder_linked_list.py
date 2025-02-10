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
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # revert second part
        second = slow.next # Head of the seocnd part
        prev = slow.next = None # Setting the preview of the head of second part AND setting the next of the last node of the first part
        while second:
            temp = second.next
            second.next = prev # changing the next to be the preview node
            prev = second # the new preview is going to be the current node from the second part
            second = temp # the new current node, from second part will be the preview's next, stored in temp

        # merge two parts
        first, second = head, prev
        while second:
            temp_1, temp_2 = first.next, second.next # from the first node of each first and second part, get their next nodes, storing them into temp variables
            first.next = second
            second.next = temp_1
            first = temp_1
            second = temp_2

