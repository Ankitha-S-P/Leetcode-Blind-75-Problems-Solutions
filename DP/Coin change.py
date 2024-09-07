#https://leetcode.com/problems/coin-change/

#Memoization --- takes up extra stack auxilliary space
class Solution:
              
    def coinChange(self, coins: List[int], amount: int) -> int:
        ###################################################
        def f(ind,amount,arr,dp):
            if ind==0:
                if amount%arr[ind]==0:
                    dp[ind][amount]=amount//arr[ind]
                    return dp[ind][amount]
                else:
                    return 1e9
            if dp[ind][amount]!=-1:
                return dp[ind][amount]
            notake=0+f(ind-1,amount,arr,dp)
            take=float('inf')
            if arr[ind]<=amount:
                take=1+f(ind,amount-arr[ind],arr,dp)
            dp[ind][amount]=min(notake,take)    
            return dp[ind][amount]
        ####################################################
        dp=[[-1]*(amount+1) for _ in range(len(coins))]
        f(len(coins)-1,amount,coins,dp)
        if dp[len(coins)-1][amount]>=1e9:
            return -1
        else:
            return dp[len(coins)-1][amount]

#tabulation ---- no extra auxilliary stack space but space complexity is still be O(m*n)
class Solution:
              
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[[-1]*(amount+1) for _ in range(len(coins))]
        for i in range(amount+1):
            if i%coins[0]==0:
                dp[0][i]=i//coins[0]
            else:
                dp[0][i]=1e9
        for i in range(1,len(coins)):
            for j in range(amount+1):
                    notake=0+dp[i-1][j]
                    take=float('inf')
                    if coins[i]<=j:
                        take=1+dp[i][j-coins[i]]
                    dp[i][j]=min(notake,take)         
        
        if dp[len(coins)-1][amount]>=1e9:
            return -1
        else:
            return dp[len(coins)-1][amount]    


#best method
class Solution:    
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize the dp array for the amount
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins needed to make amount 0
        for coin in coins:
            # if you can form the amount j - coin with a certain number of coins, 
              then to form the amount j, you can just add 1 coin (the current coin).
            for j in range(coin, amount + 1):
                dp[j] = min(dp[j], dp[j - coin] + 1)
        
        # If dp[amount] is still infinity, no solution was found
        return dp[amount] if dp[amount] != float('inf') else -1

