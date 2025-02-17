# URL https://neetcode.io/problems/depth-of-binary-tree
# Time Complexity: O(n)
# Space Complexity: O(h) where h is between log(n) (balanced case) and n (worst case)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode], depth=0) -> int:

        if not root:
            return depth

        depth += 1
        left_depth = self.maxDepth(root.left, depth)
        right_depth = self.maxDepth(root.right, depth)

        return left_depth if left_depth > right_depth else right_depth
