# URL https://neetcode.io/problems/count-good-nodes-in-binary-tree
# Time Complexity: O(n)
# Space Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# root=[3,3,null,4,2]
#         3
#       / \
#      3  
#     / \
#    4   2

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        qty_good_nodes = 0

        def dfs(node, max_value):
            nonlocal qty_good_nodes
            if not node:
                return None
            if node.val >= max_value:
                qty_good_nodes += 1
                max_value = node.val
            dfs(node.left, max_value)
            dfs(node.right, max_value)

        dfs(root, float('-inf'))
        return qty_good_nodes
