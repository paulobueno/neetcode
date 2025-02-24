# URL https://neetcode.io/problems/count-good-nodes-in-binary-tree
# Time Complexity: O(n)
# Space Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, min_value, max_value):

            if not node:
                return True

            if node.val <= min_value or node.val >= max_value:
                return False
            if node.left and node.left.val >= node.val:
                return False
            if node.right and node.right.val <= node.val:
                return False

            return dfs(node.left, min_value, min(node.val, max_value)) and dfs(node.right, max(min_value, node.val), max_value)

        return dfs(root, float('-inf'), float('inf'))
