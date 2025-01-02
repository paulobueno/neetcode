# URL https://neetcode.io/problems/validate-parentheses
# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        stack = []
        open_chars = '({['
        pair = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for c in s:
            if c in open_chars:
                stack.append(c)
            else:
                if len(stack) and stack[-1] == pair.get(c):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
