# URL https://neetcode.io/problems/combination-target-sum
# Time Complexity: O(2^target)
# Space Complexity: O(2^target)

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, curr, total):
            if total == target:
                result.append(curr.copy())
                return
            elif total > target or i >= len(nums):
                return

            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            curr.pop()
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return result
