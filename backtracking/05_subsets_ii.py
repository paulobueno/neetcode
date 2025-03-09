# URL https://neetcode.io/problems/subsets-ii
# Time Complexity: O(n*2^n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def dfs(i, comb):
            if i == len(nums):
                result.append(comb.copy())
                return
            comb.append(nums[i])
            dfs(i + 1, comb)
            comb.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, comb)


        dfs(0, [])
        return result
        
