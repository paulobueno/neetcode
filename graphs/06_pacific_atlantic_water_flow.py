# URL https://neetcode.io/problems/pacific-atlantic-water-flow
# Time Complexity: O(m*n) m -> rows n -> columns
# Space Complexity: O(m*n)

from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set() # means that the position can reach Pacific or Atlantic

        def dfs(i, j, visit, prev_height):
            if (i not in range(ROWS)
                or j not in range(COLS)
                or (i, j) in visit
                or heights[i][j] < prev_height):
                return
            visit.add((i, j))
            dfs(i + 1, j, visit, heights[i][j])
            dfs(i - 1, j, visit, heights[i][j])
            dfs(i, j + 1, visit, heights[i][j])
            dfs(i, j - 1, visit, heights[i][j])

        # Check Left (Pacific) and Right (Atlantic) sides of the matrix
        for i in range(ROWS):
            dfs(i, 0, pac, 0)
            dfs(i, COLS - 1, atl, 0)

        # Check Top (Pacific) and Bottom (Atlantic) sides of the matrix
        for j in range(COLS):
            dfs(0, j, pac, 0)
            dfs(ROWS - 1, j, atl, 0)

        result = []
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) in pac and (i, j) in atl:
                    result.append([i, j])

        return result
