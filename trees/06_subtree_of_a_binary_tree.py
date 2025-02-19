# URL https://neetcode.io/problems/subtree-of-a-binary-tree
# Time Complexity: O(n*m)
# Space Complexity: O(n+m)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def are_trees_equal(self, root_1, root_2):
        if not root_1 and not root_2:
            return True
        elif not root_1 or not root_2:
            return False

        left = self.are_trees_equal(root_1.left, root_2.left)
        right = self.are_trees_equal(root_1.right, root_2.right)
        return left and right and (root_1.val == root_2.val)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        elif not root or not subRoot:
            return False

        if root.val == subRoot.val and self.are_trees_equal(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
