# URL https://neetcode.io/problems/two-integer-sum-ii
# Time Complexity: O(N)
# Space Complexity: O(N)
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while numbers[left] + numbers[right] != target:
            if numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return [left + 1, right + 1]

if __name__ == "__main__":
    print(Solution().twoSum([2,3,4], 6)) # [1, 3]