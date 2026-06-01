class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        peak = prices[n-1]
        max_profit = 0
        for i in range(n-2, -1, -1):
            cur =  prices[i]
            print(f"cur:{cur}")
            peak = max(peak, cur)
            print(f"peak:{peak}")
            tmp = peak - cur
            print(f"tmp:{tmp}")
            max_profit = max(max_profit, tmp)
            print(f"max_profit:{max_profit}\n")
        return max_profit


#prices=[7,1,5,3,6,4]
    