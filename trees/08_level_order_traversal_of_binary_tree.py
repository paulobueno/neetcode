# URL https://neetcode.io/problems/level-order-traversal-of-binary-tree
# Time Complexity: O(n)
# Space Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        nodes =[[1, root]]
        hight = 1
        for node in nodes:
            hight = max(hight, node[0])
            if node[1].left:
                nodes.append([node[0] + 1, node[1].left])
            if node[1].right:
                nodes.append([node[0] + 1, node[1].right])

        grouped_nodes = [[] for _ in range(hight)]
        for node in nodes:
            grouped_nodes[node[0]-1].append(node[1].val)

        return grouped_nodes

