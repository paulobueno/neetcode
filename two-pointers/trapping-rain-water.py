# URL https://neetcode.io/problems/trapping-rain-water
# Time Complexity: O(N)
# Space Complexity: O(1)

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_left = 0
        max_right = 0
        water = 0
        while left <= right:
            if max_left <= max_right:
                water += max_left - height[left] if max_left - height[left] > 0 else 0
                max_left = max(max_left, height[left])
                left += 1
            else:
                water += max_right - height[right] if max_right - height[right] > 0 else 0
                max_right = max(max_right, height[right])
                right -= 1
        return water

if __name__ == '__main__':
    print(Solution().trap([0,2,0,3,1,0,1,3,2,1])) # 9
    print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
    print(Solution().trap([5,4,1,2])) # 1

