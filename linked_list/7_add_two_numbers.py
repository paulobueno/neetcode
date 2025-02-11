# URL https://neetcode.io/problems/add-two-numbers
# Time Complexity: O(n+m)
# Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_sum = 0
        l2_sum = 0
        qty = 0
        while l1:
            l1_sum += (l1.val * (10**qty))
            l1 = l1.next
            qty += 1
        qty = 0
        while l2:
            l2_sum += (l2.val * (10**qty))
            l2 = l2.next
            qty += 1
        total_sum = l1_sum + l2_sum

        head = prev = ListNode(int(str(total_sum)[-1]))
        for num in reversed(str(total_sum)[:-1]):
            curr_node = ListNode(int(num))
            prev.next = curr_node
            prev = curr_node

        return head
