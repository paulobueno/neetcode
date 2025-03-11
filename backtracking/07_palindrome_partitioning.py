# URL https://neetcode.io/problems/palindrome-partitioning
# Time Complexity: O(x)
# Space Complexity: O(x)

from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result, part = [], []

        def dfs(i):
            if i >= len(s):
                result.append(part.copy())
                return

            for j in range(i, len(s)):
                substring = s[i:j+1]
                is_palindrome = substring == substring[::-1]
                if is_palindrome:
                    part.append(substring)
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return result


