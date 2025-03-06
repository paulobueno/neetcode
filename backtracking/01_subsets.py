# URL https://neetcode.io/problems/invert-a-binary-tree
# Time Complexity: O(n*2^n)
# Space Complexity: O(n)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)

        dfs(0)
        return result
