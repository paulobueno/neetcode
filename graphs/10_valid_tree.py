# URL https://neetcode.io/problems/valid-tree
# Time Complexity: O(m*n) m -> rows n -> columns
# Space Complexity: O(m*n)

from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        tree_map = {i: [] for i in range(n)}
        for a, b in edges:
            tree_map[a].append(b)
            tree_map[b].append(a)

        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False

            visited.add(node)
            for edge in tree_map[node]:
                if edge == prev:
                    continue
                if dfs(edge, node) is False:
                    return False

            return True

        return dfs(next(iter(tree_map.keys())), None) and n == len(visited)

if __name__ == '__main__':
    n = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    print(Solution().validTree(n, edges)) # True
