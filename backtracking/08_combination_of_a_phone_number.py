# URL https://neetcode.io/problems/combinations-of-a-phone-number
# Time Complexity: O(n*4^n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_map = {
                   2: 'abc',
                   3: 'def',
                   4: 'ghi',
                   5: 'jkl',
                   6: 'mno',
                   7: 'pqrs',
                   8: 'tuv',
                   9: 'wxyz'
                }
        result, word = [], []


        def dfs(i):
            if i >= len(digits):
                if word:
                    result.append(''.join(word))
                return

            for letter in letter_map[int(digits[i])]:
                word.append(letter)
                dfs(i + 1)
                word.pop()

        dfs(0)
        return result

