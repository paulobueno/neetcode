# URL https://neetcode.io/problems/string-encode-and-decode
# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word)) + "#" + word
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        curr_char = 0
        while curr_char < len(s):
            word_length = ""
            while s[curr_char] != "#":
                word_length += s[curr_char]
                curr_char += 1
            curr_char += 1
            result.append(s[curr_char:curr_char + int(word_length)])
            curr_char += int(word_length)
        return result
            
