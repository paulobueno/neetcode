# URL https://neetcode.io/problems/top-k-elements-in-list
# Time Complexity: O(N)
# Space Complexity: O(N)

from collections import defaultdict

class Solution:

    def flatten(self, lst_of_lst):
        for lst in lst_of_lst:
            for el in lst:
                yield el

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = [[] for _ in range(len(nums))]
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        for key, value in freq.items():
            groups[len(nums) - value].append(key)

        result = []
        for n in self.flatten(groups):
            result.append(n)
            if len(result) == k:
                break

        return result


