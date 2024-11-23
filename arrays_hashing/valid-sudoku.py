# URL https://neetcode.io/problems/valid-sudoku
# Time Complexity: O(N)
# Space Complexity: O(1)

from copy import copy, deepcopy

class Solution:

    @staticmethod
    def get_square_index(i, j):
        return j//3 + (3 * (i//3))

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        num_dict = {key: False for key in range(1, 10)}
        row_validation = {key: copy(num_dict) for key in range(len(board))}
        column_validation = deepcopy(row_validation)
        square_validation = deepcopy(row_validation)

        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num != ".":

                    if row_validation[i][int(num)]:
                        return False
                    else:
                        row_validation[i][int(num)] = True

                    if column_validation[j][int(num)]:
                        return False
                    else:
                        column_validation[j][int(num)] = True

                    if square_validation[self.get_square_index(i, j)][int(num)]:
                        return False
                    else:
                        square_validation[self.get_square_index(i, j)][int(num)] = True

        return True



