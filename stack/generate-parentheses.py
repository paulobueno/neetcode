# URL https://neetcode.io/problems/generate-parentheses
# Time Complexity: O((4^2N)/N^0.5)
# Space Complexity: O(N)
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtracking(open_count: int, close_count: int) -> None:
            if open_count == close_count == n:
                res.append(''.join(stack))
                return

            if open_count < n:
                stack.append("(")
                backtracking(open_count + 1, close_count)
                stack.pop()
            if close_count < open_count:
                stack.append(")")
                backtracking(open_count, close_count + 1)
                stack.pop()

        backtracking(0, 0)
        return res


if __name__ == "__main__":
    print(Solution().generateParenthesis(4))
