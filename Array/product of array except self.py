#https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[1]*len(nums)
        n=len(nums)
        temp=1
        for i in range(1,len(nums)):
            ans[i]=ans[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            temp*=nums[i+1]
            ans[i]*=temp
        return ans    
      
#Time complexity:O(N)
#Space complexity:O(N)
