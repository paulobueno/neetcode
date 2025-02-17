# URL https://neetcode.io/problems/merge-k-sorted-linked-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Time Complexity: O(n*k)
# Space Complexity: O(1)
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = last = ListNode()
        while any(lists):
            temp = ListNode(float("inf"))
            index = None
            for i, node in enumerate(lists):
                if node and node.val < temp.val:
                    temp = node
                    index = i
            lists[index] = lists[index].next
            last.next = temp
            last = temp
        return dummy.next


# Time Complexity: O(n*log(k))
# Space Complexity: O(k)
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not any(lists):
            return None
        
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                merged_lists.append(self.merge_lists(l1, l2))
            lists = merged_lists

        return lists[0]

    def merge_lists(self, l1, l2):
        dummy = tail = ListNode()

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next
