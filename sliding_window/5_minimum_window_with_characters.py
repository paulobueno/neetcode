# URL https://neetcode.io/problems/minimum-window-with-characters
# Time Complexity: O(n)
# Space Complexity: O(m)

"""
Returns s`s shortest substring that contains all characters of t
if not substring is found, return ""
"""

from typing import List

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        seek_map = {}
        for letter in t:
            seek_map[letter] = seek_map.get(letter, 0) + 1

        match = 0
        need_match = len(seek_map.keys())
        curr_count = {}
        l = r = 0
        substring = None
        curr_count[s[r]] = curr_count.get(s[r],0) + 1
        if curr_count[s[r]] == seek_map.get(s[r]):
            match += 1

        while True:

            if match == need_match:
                if substring is None:
                    substring = s[l:r+1]
                elif len(s[l:r+1]) < len(substring):
                    substring = s[l:r+1]
                l += 1
                if not l < len(s):
                    break
                if curr_count[s[l-1]] == seek_map.get(s[l-1]):
                    match -= 1
                curr_count[s[l-1]] -= 1
            else:
                r += 1
                if not r < len(s):
                    break
                curr_count[s[r]] = curr_count.get(s[r],0) + 1
                if curr_count[s[r]] == seek_map.get(s[r]):
                    match += 1

        return substring if substring is not None else ""


if __name__ == "__main__":
    print(Solution().minWindow("OUZODYXAZV","XYZ")=="YXAZ")
    print(Solution().minWindow("xyz","xyz")=="xyz")
    print(Solution().minWindow("x","xy")=="")
    print(Solution().minWindow("abczuzuzuzuauzuzubzuzuzc","abc")=="abc")
