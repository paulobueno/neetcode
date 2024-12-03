# URL https://neetcode.io/problems/longest-consecutive-sequence
# Time Complexity: O(N)
# Space Complexity: O(N)

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for num in nums_set:
            qty = 0
            curr_num = num
            is_sequence_start = not curr_num - 1 in nums_set
            if is_sequence_start:
                while curr_num in nums_set:
                    qty += 1
                    curr_num += 1
                if qty > longest:
                    longest = qty
        return longest

if __name__ == "__main__":
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    solution = Solution()
    print(solution.longestConsecutive(nums)) # 9
