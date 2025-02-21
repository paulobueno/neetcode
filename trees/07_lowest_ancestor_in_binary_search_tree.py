# URL https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree
# Time Complexity: O(x)
# Space Complexity: O(x)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# SOLUTION IF IT WOULD BE A BINARY TREE THAT DONT FOLLOWS BINARY SEARCH TREE RULES (LEFT ALWAYS LOWER THAN RIGHT)
#        8
#       / \
#      2   3
#     / \ / \
#    1  9 4  5
class Solution:
    def generate_node_stack(self, root, seek_node, stack=None):
        if stack is None:
            stack = []
        stack.append(root)

        if not root:
            return [False, stack]

        if root.val == seek_node.val:
            return [True, stack]

        if self.generate_node_stack(root.left, seek_node, stack)[0]:
            return [True, stack]
        else:
            stack.pop()

        if self.generate_node_stack(root.right, seek_node, stack)[0]:
            return [True, stack]
        else:
            stack.pop()

        return [False, stack]

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_stack = self.generate_node_stack(root, p)[1]
        q_stack = self.generate_node_stack(root, q)[1]
        i = 0
        while i < len(p_stack) and i < len(q_stack) and p_stack[i].val == q_stack[i].val:
            i += 1
        return p_stack[i-1]



# if __name__ == "__main__":
#     root = TreeNode(8)
#     root.left = TreeNode(2)
#     root.right = TreeNode(3)
#     root.left.left = TreeNode(1)
#     root.left.right = TreeNode(9)
#     root.right.left = TreeNode(4)
#     root.right.right = TreeNode(5)
#     stack = Solution().generate_node_stack(root, root.left.right)[1]




