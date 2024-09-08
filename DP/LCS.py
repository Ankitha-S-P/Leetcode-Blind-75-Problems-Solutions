#https://leetcode.com/problems/longest-common-subsequence/
#memoisation
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def f(n1,n2,dp):
            if n1<0 or n2<0:
                return 0
            #check if already calculated
            if dp[n1][n2]!=-1:
                return dp[n1][n2]    
            #match
            if text1[n1]==text2[n2]:
                count=1+f(n1-1,n2-1,dp)
            #no match
            else:
                count=0+max(f(n1,n2-1,dp),f(n1-1,n2,dp))
            dp[n1][n2]=count     
            return dp[n1][n2]

        dp=[[-1]*len(text2) for _ in range(len(text1))]        
        return f(len(text1)-1,len(text2)-1,dp)

 #tabulation or algorithm for LCS
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 if i == 0 or j == 0 else -1 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
            #match    
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
            #no match
                else:
                    dp[i][j]=0+max(dp[i][j-1],dp[i-1][j])
                 
        return dp[len(text1)][len(text2)]
