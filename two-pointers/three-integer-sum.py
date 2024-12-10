# URL https://neetcode.io/problems/three-integer-sum
# Time Complexity: O(N^2)
# Space Complexity: O(1)

from typing import List
from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and nums[i-1] == num:
                continue

            l, r = i+1, len(nums)-1
            while l < r:
                if num + nums[l] + nums[r] > 0:
                    r -= 1
                elif num + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    result.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l-1] == nums[l] and l < r:
                        l += 1

        return result



