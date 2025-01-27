# URL https://neetcode.io/problems/longest-substring-without-duplicates
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        letters = set()
        l = 0
        for r in range(len(s)):
            while s[r] in letters:
                letters.remove(s[l])
                l += 1
            letters.add(s[r])
            res = max((r-l)+1,res)
        return res


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("zxyzxyz")==3)
    print(Solution().lengthOfLongestSubstring("dvdf")==3)
