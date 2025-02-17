# URL https://neetcode.io/problems/binary-tree-diameter
# Time Complexity: O(n)
# Space Complexity: O(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.length = 0

    def get_depth(self, root):
        if not root:
            return 0
        left = self.get_depth(root.left)
        right = self.get_depth(root.right)
        self.length = max(self.length, left + right)
        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.get_depth(root)
        return self.length

