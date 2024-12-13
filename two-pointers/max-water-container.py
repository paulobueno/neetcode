# URL https://neetcode.io/problems/max-water-container
# Time Complexity: O(N)
# Space Complexity: O(1)

from typing import List

class Solution:

    def maxArea(self, heights: List[int]) -> int:
        volume = 0
        left, right = 0, len(heights) - 1
        while left < right:
            curr_volume = (right - left) * min(heights[left], heights[right])
            if curr_volume > volume:
                volume = curr_volume
            if heights[left] >= heights[right]:
                right -= 1
            else:
                left += 1
        return volume

if __name__ == '__main__':
    print(Solution().maxArea([1,7,2,5,4,7,3,6])) # 36
