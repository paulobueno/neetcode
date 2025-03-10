# URL https://neetcode.io/problems/balanced-binary-tree
# Time Complexity: O(n)
# Space Complexity: O(k) k = (n + log(n)) / 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def dfs(self, root: TreeNode):
        if not root:
            return [True, 0]
        left, right = self.dfs(root.left), self.dfs(root.right)
        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        depth = max(left[1], right[1]) + 1
        return [balanced, depth]

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[0]
        
