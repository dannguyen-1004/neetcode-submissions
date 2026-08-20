class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        prof = 0
        i = 0

        for j in range(1, len(prices)):
            diff = prices[j] - prices[i]
            if diff > prof:
                prof = diff
            if prices[j] < prices[i]:
                i = j
            
        return prof

        