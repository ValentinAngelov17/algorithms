class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for day in range(len(prices)):
            buy = prices[day]
            max_profit = max(prices[day:])
            current_profit = max_profit - buy

            if current_profit >= profit:
                profit = current_profit

        return profit


a = Solution()
print(a.maxProfit(prices=[7,6,4,3,1]))
