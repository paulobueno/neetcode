# URL https://neetcode.io/problems/anagram-groups
# Time Complexity: O(N)
# Space Complexity: O(N)

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            letters_count = [0] * 256
            for letter in word:
                letters_count[ord(letter)] += 1
            groups[tuple(letters_count)].append(word)
        return list(groups.values())
        
