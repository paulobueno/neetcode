# URL https://neetcode.io/problems/rotting-fruit
# Time Complexity: O(r*c) where r = rows and c = columns
# Space Complexity: O(r*c)
from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        moves = [[1,0],[-1,0],[0,1],[0,-1]]
        fresh = 0
        time = 0
        q = deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j))

        while q and fresh > 0:
            for _ in range(len(q)):
                i, j = q.popleft()
                for move in moves:
                    new_i = i + move[0]
                    new_j = j + move[1]
                    in_boundary = new_i in range(ROWS) and new_j in range(COLS)

                    if in_boundary and grid[new_i][new_j] == 1:
                        grid[new_i][new_j] = 2
                        fresh -= 1
                        q.append((new_i, new_j))
            time += 1

        return time if fresh == 0 else -1

if __name__ == '__main__':
    print(Solution().orangesRotting([[1,1,0],[0,1,1],[0,1,2]])) # 4
