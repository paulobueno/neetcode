# URL https://neetcode.io/problems/duplicate-integer
# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        results ={}
        for num in nums:
            if results.get(num):
                return True
            results[num] = True
        return False
