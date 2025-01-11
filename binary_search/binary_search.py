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
        return l if l < len(nums) and nums[l] == target else -1

if __name__ == '__main__':
    print(Solution().search([1,49,90,100,112], 90) == 2)
    print(Solution().search([30,100,200,300], 310) == -1)
    print(Solution().search([30,100,200,300], 150) == -1)
