# URL https://neetcode.io/problems/binary-tree-right-side-view
# Time Complexity: O(n)
# Space Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def bfs(nodes):
            if not nodes:
                return None
            last_node = None
            len_nodes = len(nodes)
            for i, node in enumerate(nodes[:len_nodes]):
                if node:
                    last_node = node
                    nodes.append(node.left)
                    nodes.append(node.right)
            if last_node:
                result.append(last_node.val)
            bfs(nodes[len_nodes:])

        bfs([root])
        return result
