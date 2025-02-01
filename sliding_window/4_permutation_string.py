# URL https://neetcode.io/problems/permutation-string
# Time Complexity: O(26*n)
# Space Complexity: O(m)

from typing import List

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        l, r = 0, len(s1) - 1
        s1_count = {}
        s2_count = {}

        for i in range(r + 1):
            s1_count[s1[i]] = s1_count.get(s1[i], 0) + 1
            s2_count[s2[i]] = s2_count.get(s2[i], 0) + 1

        while r < len(s2) - 1:
            if s1_count == s2_count:
                return True
            s2_count[s2[l]] -= 1
            if s2_count[s2[l]] == 0:
                del s2_count[s2[l]]
            l += 1
            r += 1
            s2_count[s2[r]] = s2_count.get(s2[r], 0) + 1

        return s1_count == s2_count



if __name__ == '__main__':
    print(Solution().checkInclusion("abc", "lecabee")==True)
    print(Solution().checkInclusion("abc", "lecaabee")==False)
    print(Solution().checkInclusion("adc", "dcda")==True)
