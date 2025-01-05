# URL https://neetcode.io/problems/daily-temperatures
# Time Complexity: O(N)
# Space Complexity: O(N)
"""
LEARNINGS
Elements added to stack has always a lower value compared to other elements in the stack.
This happens because we only append the current element after popping all lower elements (rows 13:15)
Due to this fact, there is no reason to iterate to all elements in the stack but only the last one.
As there is no need to read all elements in the stack every iteration, the time complexity is N instead of N^2
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []
        for curr_i, curr_temp in enumerate(temperatures):
            while stack and curr_temp > stack[-1][1]:
                output[stack[-1][0]] = curr_i - stack[-1][0]
                stack.pop()
            stack.append((curr_i, curr_temp))
        return output
