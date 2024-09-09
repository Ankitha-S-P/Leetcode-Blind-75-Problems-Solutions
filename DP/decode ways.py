#https://leetcode.com/problems/decode-ways/

#memoisation
class Solution:
    def numDecodings(self, s: str) -> int:
        def f(n):
            if n==len(s):
                return 1    
            #one digit
            if s[n]=='0':
                return 0
            if dp[n]!=-1:
                return dp[n]    
            one=f(n+1)
            #two digit
            two=0
            if n+1<len(s):               
                if s[n]=='2' and s[n+1]<='6' or s[n]=='1':
                        two=f(n+2)
            dp[n]=one+two
            return dp[n]
        dp=[-1 for _ in range(len(s))]             
        return f(0)  
      
#tabulation
class Solution:
    def numDecodings(self, s: str) -> int:
        dp=[1 if i==len(s) else -1 for i in range(len(s)+1)]
        for i in range(len(s)-1,-1,-1):
            if s[i]=='0':
                dp[i]=0
            else:
                one=dp[i+1]
            #two digit
                two=0
                if i+1<len(s):               
                    if s[i]=='2' and s[i+1]<='6' or s[i]=='1':
                        two=dp[i+2]
                dp[i]=one+two
        return dp[0]    

#space optimisation
class Solution:
    def numDecodings(self, s: str) -> int:
        next1=1
        next2=1
        for i in range(len(s)-1,-1,-1):
            if s[i]=='0':
                current=0
            else:
            #one digit
                one=next1
            #two digit
                two=0
                if i+1<len(s):               
                    if s[i]=='2' and s[i+1]<='6' or s[i]=='1':
                        two=next2
                current=one+two
            next2=next1
            next1=current    
        return  next1   
