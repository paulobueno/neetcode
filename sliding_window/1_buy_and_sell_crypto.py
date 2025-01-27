# URL https://neetcode.io/problems/buy-and-sell-crypto
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        if len(prices) < 2:
            return max_profit

        l, r = 0, 1
        while r < len(prices):
            if prices[l] < prices[r]:
                new_profit = prices[r] - prices[l]
                max_profit = max(max_profit, new_profit)
            else:
                l = r
            r += 1

        return max_profit
        
if __name__ == '__main__':
    print(Solution().maxProfit([10,1,5,6,7,1])==6)

           
