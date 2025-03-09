# URL https://neetcode.io/problems/permutations
# Time Complexity: O(n!*n)
# Space Complexity: O(n!*n)

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def dfs(perm, used):
            if len(perm) == len(nums):
                result.append(perm.copy())
                return

            for i, num in enumerate(nums):
                if not used[i]:
                    used[i] = True
                    perm.append(num)
                    dfs(perm, used)
                    perm.pop()
                    used[i] = False


        dfs([], [False] * len(nums))
        return result

