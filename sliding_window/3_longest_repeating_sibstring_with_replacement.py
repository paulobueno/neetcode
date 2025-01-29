# URL https://neetcode.io/problems/longest-repeating-substring-with-replacement
# Time Complexity: O(n)
# Space Complexity: O(m)

from typing import List

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_map = {}
        max_substring = max_frequency = l = 0
        for r, letter in enumerate(s):
            count_map[letter] = count_map.get(letter, 0) + 1
            max_frequency = max(count_map[letter], max_frequency)
            while (r - l + 1) - max_frequency > k:
                count_map[s[l]] -= 1
                l += 1
            max_substring = max((r - l + 1), max_substring)
        return max_substring


if __name__ == '__main__':
    print(Solution().characterReplacement("AAABABB",1)==5)
    print(Solution().characterReplacement("XYYX",2)==4)
    print(Solution().characterReplacement("AAAABBBBBAAAA",2)==7)

