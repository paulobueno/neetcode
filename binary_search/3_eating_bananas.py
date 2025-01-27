# URL https://neetcode.io/problems/eating-bananas
# Time Complexity: O(log(max(n))*n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_rate = max(piles)
        l, r = 1, max(piles)

        while l < r:
            m = l+((r-l)//2)
            time_spent = 0
            for pile in piles:
                time = pile//m + (1 if pile%m > 0 else 0)
                time_spent += time
            if time_spent <= h:
                min_rate = min(m, min_rate)
                r = m
            else:
                l = m + 1
        
        return min_rate

