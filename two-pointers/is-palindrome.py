# URL https://neetcode.io/problems/is-palindrome
# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = "1234567890abcdefghijklmnopqrstuvxywz"
        s = [letter.lower() for letter in s if letter.lower() in letters]
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

if __name__ == "__main__":
    Solution().isPalindrome("Was it a car or a cat I saw?")
