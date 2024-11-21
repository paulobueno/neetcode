# URL https://neetcode.io/problems/two-integer-sum
# Time Complexity: O(N)
# Space Complexity: O(N)

from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = defaultdict(list)

        for i, num in enumerate(nums):
            diffs[target - num].append(i)

        for i, num in enumerate(nums):
            if diffs.get(num) and diffs.get(num)[0] != i:
                return sorted([diffs.get(num)[0], i])
