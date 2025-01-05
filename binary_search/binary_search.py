# URL https://neetcode.io/problems/binary-search
# Time Complexity: O(log(N))
# Space Complexity: O(1)

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            m = l + ((r - l) // 2)
            if nums[m] >= target:
                r = m
            else:
                l = m + 1
        return l if (l < len(nums) and nums[l] == target) else -1
