# URL https://neetcode.io/problems/surrounded-regions
# Time Complexity: O(m*n) m -> rows n -> columns
# Space Complexity: O(m*n)

from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(i, j):
            if (i not in range(ROWS)
                or j not in range(COLS)
                or board[i][j] != "O"):
                return

            board[i][j] = "T"
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        # Start DFS from each X from edges
        for i in range(ROWS):
            for j in range(COLS):
                is_in_edge = (i in [0, ROWS - 1] or j in [0, COLS - 1])
                if is_in_edge and board[i][j] == "O":
                    dfs(i, j)

        # Change O -> X and T -> O
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"

