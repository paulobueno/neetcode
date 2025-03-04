# URL https://neetcode.io/problems/kth-smallest-integer-in-bst
# Time Complexity: O(n)
# Space Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def dfs(node, k, node_number=0):
            if not node:
                return [None, node_number]

            left = dfs(node.left, k, node_number)
            node_number = left[1]
            if node_number == k:
                return left

            node_number += 1
            if node_number == k:
                return [node, node_number]

            right = dfs(node.right, k, node_number)
            node_number = right[1]
            if node_number == k:
                return right

            return [node, node_number]

        return dfs(root, k)[0].val

            

