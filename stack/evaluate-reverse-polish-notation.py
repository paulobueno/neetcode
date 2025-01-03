# URL https://neetcode.io/problems/evaluate-reverse-polish-notation
# Time Complexity: O(N)
# Space Complexity: O(N)

"""
LEARNINGS:

1. // operator
// operator performs a floor division, meaning that it rounds results towards infinite negative
so, the result of the operation 5//-100 would be -1 and not 0, as expected in the exercise

2. .isdigit() and .isnumeric():
both string methods return False to a string representing a negative number
the difference between these methods is that isdigit() checks if the string is in "0123456789"
while .isnumeric() also checks if is a Unicode symbol representing a number, such as ⅓ and ², and other numeric symbols
such as 四 (four in japanese)
"""

from typing import List


class Solution:
    OPERATORS = "+-*/"
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            negative = False
            if len(token) >= 2 and token[0] == "-":
                negative = True
                token = token[1:]
            if token.isnumeric():
                if negative:
                    stack.append(-int(token))
                else:
                    stack.append(int(token))
            if token in self.OPERATORS and len(stack) >= 2:
                first = stack.pop()
                second = stack.pop()
                result = None
                if token == "-":
                    result = second - first
                if token == "+":
                    result = second + first
                if token == "*":
                    result = second * first
                if token == "/":
                    result = int(second / first)
                stack.append(result)
        return stack[-1] if len(stack) else None



if __name__ == '__main__':
    print(Solution().evalRPN(["1", "2", "+", "3", "*", "4", "-"]))  # 5
    print(Solution().evalRPN(["4","13","5","/","+"]))  # 6
    print(Solution().evalRPN(["18"]))  # 18
    print(Solution().evalRPN(["3","-4","+"]))  # -1
    print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))  # 22
