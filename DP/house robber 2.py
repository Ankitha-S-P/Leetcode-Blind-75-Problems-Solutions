#memoisation
class Solution:
    def rob(self, nums: List[int]) -> int:
        def f(n,front):
            if n==front-1 or n==front-2:
                return 0
            if dp[n]!=-1:
                return dp[n]    
            #not take
            notake=0+f(n-1,front)
            #take
            take=nums[n]+f(n-2,front)
            dp[n]=max(notake,take)
            return dp[n]
        if len(nums)==1:
            return nums[0]        
        dp=[-1 for i in range(len(nums))] 
        ans1=f(len(nums)-2,0)
        dp=[-1 for i in range(len(nums))]  
        ans2=f(len(nums)-1,1)
        return max(ans1,ans2) 
#tabulation
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
                    
        dp=[0 if i<=1 else -1 for i in range(len(nums)+1)] 
        for i in range(2,len(nums)+1):
            notake=0+dp[i-1]
            take=nums[i-2]+dp[i-2]
            dp[i]=max(notake,take)
        ans1=dp[len(nums)]
        dp=[0 if i<=1 else -1 for i in range(len(nums)+1)]
        for i in range(2,len(nums)+1):
            notake=0+dp[i-1]
            take=nums[i-1]+dp[i-2]
            dp[i]=max(notake,take)
        ans2=dp[len(nums)]     
        return max(ans1,ans2)
#space optimisation
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        pre=pre2=0             
        for i in range(2,len(nums)+1):
            notake=0+pre
            take=nums[i-2]+pre2
            current=max(notake,take)
            pre2=pre
            pre=current
        ans1=pre
        pre=pre2=0
        for i in range(2,len(nums)+1):
            notake=0+pre
            take=nums[i-1]+pre2
            current=max(notake,take)
            pre2=pre
            pre=current
        ans2=pre   
        return max(ans1,ans2)   
