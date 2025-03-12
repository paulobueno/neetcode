# URL https://neetcode.io/problems/count-number-of-islands
# Time Complexity: O(m*n)
# Space Complexity: O(m*n)

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        movements = [(1,0),(-1,0),(0,1),(0,-1)]
        ROW, COLUMN = len(grid), len(grid[0])

        def dfs(i, j):
            if (i not in range(ROW)
                or j not in range(COLUMN)
                or grid[i][j] != '1'):
                return
            grid[i][j] = '-1'

            for move in movements:
                dfs(i + move[0], j + move[1])

        for i in range(ROW):
            for j in range(COLUMN):
                if grid[i][j] == '1':
                    dfs(i, j)
                    islands += 1

        return islands

