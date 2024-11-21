# URL https://neetcode.io/problems/is-anagram
# Time Complexity: O(N)
# Space Complexity: O(N)

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict_s, dict_t = defaultdict(int), defaultdict(int)
        s, t = list(s), list(t)

        while s:
            dict_s[s.pop()] += 1
            dict_t[t.pop()] += 1

        return dict_s == dict_t

