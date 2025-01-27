# URL https://neetcode.io/problems/find-minimum-in-rotated-sorted-array
# Time Complexity: O(x)
# Space Complexity: O(x)

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + ((r-l)//2)
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]

if __name__ == '__main__':
    print(Solution().findMin([2,3,4,0,1]) == 0)
