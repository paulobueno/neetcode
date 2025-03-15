# URL https://neetcode.io/problems/islands-and-treasure
# Time Complexity: O(m*n)
# Space Complexity: O(m*n)

from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()

        # add treasures to the queue
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    visited.add((i, j))
                    q.append((i, j))

        def next_step(i, j):
            if (i not in range(ROWS)
                or j not in range(COLS)
                or (i, j) in visited
                or grid[i][j] == -1):
                return
            q.append((i, j))
            visited.add((i, j))

        dist = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                grid[i][j] = dist
                next_step(i + 1, j)
                next_step(i - 1, j)
                next_step(i, j + 1)
                next_step(i, j - 1)
            dist += 1
