#https://leetcode.com/problems/unique-paths/

#recursion
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:        
        def f(i,j):
            if i==m-1 and j==n-1:
                count[0]+=1
                return                    
            #right 
            r=0      
            if j<n-1:
                f(i,j+1)      
            #bottom
            b=0
            if i<m-1:
                f(i+1,j)   
        count=[0]
        f(0,0)        
        return count[0]      
      
#memoisation
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:        
        def f(i,j):
            if i==m-1 and j==n-1:
                return 1                
            if dp[i][j]!=-1:
                return dp[i][j]    
            #right 
            r=0      
            if j<n-1:
                r=f(i,j+1)      
            #bottom
            b=0
            if i<m-1:
                b=f(i+1,j)
            dp[i][j]=r+b
            return dp[i][j]    
        dp=[[-1 for _ in range(n)] for _ in range(m)]        
        return f(0,0)  
      
#tabulation
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:            
        dp=[[1 if i==m-1 and j==n-1 else -1 for j in range(n)] for i in range(m)]  
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i==m-1 and j==n-1:
                    continue
                r=0      
                if j<n-1:
                    r=dp[i][j+1]      
            #bottom
                b=0
                if i<m-1:
                    b=dp[i+1][j]
                dp[i][j]=r+b          
        return dp[0][0]

#space optimisation
import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m+n-2,m-1)
