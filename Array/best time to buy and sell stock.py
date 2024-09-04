#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_element=prices[0]
        profit=float('-inf')
        for x in prices:
            min_element=min(min_element,x)
            profit=max(profit,x-min_element)
        return profit 
#Time complexity:O(N)
#Space complexity:O(1)
      
      
