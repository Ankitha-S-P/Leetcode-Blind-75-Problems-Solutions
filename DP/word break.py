
#memoisation
class Solution:
    def wordBreak(self, s: str, word: List[str]) -> bool:
        def f(n):
            if n==len(s):
                return True
            if dp[n]!=-1:
                return dp[n]                   
            check=False
            for i in range(len(word)):
                if n+len(word[i])<=len(s) and s[n:n+len(word[i])]==word[i]:
                    check=check or f(n+len(word[i]))
            dp[n]=check        
            return dp[n]
        dp=[-1 for _ in range(len(s))]         
        return f(0) 

#tabulation
class Solution:
    def wordBreak(self, s: str, word: List[str]) -> bool:
        n=len(s)    
        dp=[False]*(n+1)
        dp[n]=True
        for j in range(n-1,-1,-1):
            check=False
            for i in range(len(word)):
                if j+len(word[i])<=n and s[j:j+len(word[i])]==word[i]:
                    check=check or dp[j+len(word[i])]
            dp[j]=check        
        return dp[0]        
