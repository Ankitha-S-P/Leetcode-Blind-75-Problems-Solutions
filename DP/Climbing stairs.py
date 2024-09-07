#https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        def f(n):
            if n==0:
                return 1
            if n==1:
                return 1
            left=f(n-1)
            right=f(n-2)
            return left+right 
        return f(n) 
        this is exceeding time ...irther i can go for memoization/tabulation using a dp array dp[n] storing the values.
        more optimised space complexity for tabulation is using 3 variables. 
        THIS PROBLEM IS VERY SIMILAR TO FINDING NTH FIBONACCI NO.
        """ 
        pre=1
        pre2=1
        current=1
        for i in range(2,n+1):
            current=pre+pre2
            pre2=pre 
            pre=current
        return current 
      
#Time complexity:O(N)
#Space complexity:O(1)
