# URL https://neetcode.io/problems/max-area-of-island
# Time Complexity: O(m*n)
# Space Complexity: O(m*n)

from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(i, j):
            if (i not in range(ROWS)
                or j not in range(COLS)
                or grid[i][j] == 0
                or (i, j) in visited):
                return 0

            visited.add((i, j))
            return (1 + dfs(i + 1, j)
                      + dfs(i - 1, j)
                      + dfs(i, j + 1)
                      + dfs(i, j - 1))

        size = 0
        for i in range(ROWS):
            for j in range(COLS):
                size = max(size, dfs(i, j))

        return size
