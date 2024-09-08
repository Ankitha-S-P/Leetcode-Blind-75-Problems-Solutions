#https://leetcode.com/problems/longest-increasing-subsequence/

#memoisation
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def f(n,maxind,dp):
            if n>=len(nums):
                return 0
            if dp[n][maxind+1]!=-1:
                return dp[n][maxind+1]
            notake=0+f(n+1,maxind,dp)
            take=0
            if maxind==-1 or nums[n]>nums[maxind]:
                take=1+f(n+1,n,dp)
            dp[n][maxind+1]=max(take,notake)  
            return dp[n][maxind+1] 

        dp=[[-1]*(len(nums)+1) for _ in range(len(nums))]
        return f(0,-1,dp)         

#Time complexity: O(N*N+1) (for dp[n][n+1] all will be calculated once)
#Space complexity: O(N*N+1) + O(N) stack calls
