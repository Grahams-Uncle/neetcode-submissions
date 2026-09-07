class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxProf = 0
        minBuy = prices[0]

        for p in prices:
            if p > minBuy:
                maxProf = max(p - minBuy, maxProf)
            else:
                minBuy = p
        return maxProf

