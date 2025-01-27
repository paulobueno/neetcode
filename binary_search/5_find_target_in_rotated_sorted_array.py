# URL https://neetcode.io/problems/find-target-in-rotated-sorted-array
# Time Complexity: O(log(n))
# Space Complexity: O(1)
# NOTES:
#   Keep in mind that m is always left priority, so m could be equal to l.
#   At the base case when the array has 2 elements, the target might be the second

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + ((r-l)//2)
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1

if __name__ == '__main__':
    print(Solution().search([3,4,5,6,1,2],1)==4)
    print(Solution().search([3,1],1)==1)
