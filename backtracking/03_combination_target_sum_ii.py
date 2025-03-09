# URL https://neetcode.io/problems/combination-target-sum-ii
# Time Complexity: O(n*2**n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def dfs(i, subset, total):
            if total == target:
                result.append(subset.copy())
                return
            elif i == len(candidates) or total > target:
                return

            subset.append(candidates[i])
            dfs(i + 1, subset, total + candidates[i])
            subset.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, subset, total)

        dfs(0, [], 0)
        return result
        
if __name__ == '__main__':
    print(Solution().combinationSum2([9,2,2,4,6,1,5], 8)) # [[1,2,5],[2,2,4],[2,6]]
