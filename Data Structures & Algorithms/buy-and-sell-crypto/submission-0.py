class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        buy_at=101
        profit=0
        while i<len(prices):
            if prices[i]<buy_at:
                buy_at=prices[i]
            if prices[i]-buy_at>profit:
                profit = prices[i]-buy_at
            i+=1
        return profit