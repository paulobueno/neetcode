# URL https://neetcode.io/problems/longest-repeating-substring-with-replacement
# Time Complexity: O(n*m)
# Space Complexity: O(m)
# NOTE: There is an optimal solution using sliding window. check the website.

from typing import List

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        char_set = set(s)

        for char in char_set:
            l = count = 0
            for r in range(len(s)):
                if s[r] == char:
                    count += 1
                while (r-l+1)-count > k:
                    if s[l] == char:
                        count -= 1
                    l += 1
                res = max(res,(r-l+1))

        return res


if __name__ == '__main__':
    print(Solution().characterReplacement("AAABABB",1)==5)
    print(Solution().characterReplacement("XYYX",2)==4)
