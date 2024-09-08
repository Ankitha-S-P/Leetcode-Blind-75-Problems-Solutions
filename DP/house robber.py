#memoisation
class Solution:
    def rob(self, nums: List[int]) -> int:
        def f(n):
            if n>=len(nums):
                return 0
            if dp[n]!=-1:
                return dp[n]    
            #no take
            notake=0+f(n+1)
            #take
            take=nums[n]+f(n+2) 
            dp[n]=max(notake,take)
            return dp[n]
        dp=[-1 for _ in range(len(nums))]    
        return f(0)  
#tabulation
