class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        peak = prices[n-1]
        max_profit = 0
        for i in range(n-2, -1, -1):
            cur =  prices[i]
            peak = max(peak, cur)
            tmp = peak - cur
            max_profit = max(max_profit, tmp)
        return max_profit


#prices=[7,1,5,3,6,4]
    