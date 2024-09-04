#https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]*len(nums)
        n=len(nums)
        temp=1
        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            temp*=nums[i+1]
            prefix[i]*=temp
        return prefix    
      
#Time complexity:O(N)
#Space complexity:O(N)
