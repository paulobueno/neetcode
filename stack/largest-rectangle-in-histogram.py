# URL https://neetcode.io/problems/largest-rectangle-in-histogram
# Time Complexity: O(N)
# Space Complexity: O(N)

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i, height in enumerate(heights):
            if i == 0:
                stack.append([i, height])
                continue
            while stack and height < stack[-1][1]:
                start_i = 0 if len(stack) == 1 else stack[-2][0] + 1
                curr_area = (i - start_i) * stack[-1][1]
                if curr_area > max_area:
                    max_area = curr_area
                stack.pop()
            stack.append([i, height])

        while stack:
            i, height = stack.pop()
            start_i = stack[-1][0] + 1 if len(stack) else 0
            curr_area = (len(heights) - start_i) * height
            if curr_area > max_area:
                max_area = curr_area

        return max_area

if __name__ == '__main__':
    print(Solution().largestRectangleArea([2,1,5,6,2,3])) # 10
    print(Solution().largestRectangleArea([5,4,1,2]))  # 8
