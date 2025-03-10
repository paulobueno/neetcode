# URL https://neetcode.io/problems/search-for-word
# Time Complexity: O(b*4^w) where b == len(board) and w == len(word)
# Space Complexity: O(w)

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COLUMN = len(board), len(board[0])
        visited = set()

        def dfs(position, letter_index):
            row, column = position

            if letter_index == len(word):
                return True

            if (position in visited
                or min(position) < 0
                or row >= ROW
                or column >= COLUMN
                or board[row][column] != word[letter_index]):
                return False

            visited.add(position)
            path_result = (dfs((row + 1, column), letter_index + 1)
                           or dfs((row - 1, column), letter_index + 1)
                           or dfs((row, column + 1), letter_index + 1)
                           or dfs((row, column - 1), letter_index + 1))
            visited.remove(position)
            return path_result

        for i, row in enumerate(board):
            for j, _ in enumerate(row):
                if dfs((i, j), 0): 
                    return True

        return False

