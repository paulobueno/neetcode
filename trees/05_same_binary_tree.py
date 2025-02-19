# URL https://neetcode.io/problems/same-binary-tree
# Time Complexity: O(n)
# Space Complexity: O(k) k = (n + log(n)) / 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root_1, root_2):
        if not root_1 and not root_2:
            return True
        elif not root_1:
            return False
        elif not root_2:
            return False

        left = self.dfs(root_1.left, root_2.left)
        right = self.dfs(root_1.right, root_2.right)
        return left and right and root_1.val == root_2.val

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.dfs(p, q)
        
