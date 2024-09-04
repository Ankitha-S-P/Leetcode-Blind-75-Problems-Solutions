#https://leetcode.com/problems/maximum-subarray/submissions/1378547828/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ=0
        maxx=nums[0]
        for i in range(len(nums)):
            summ+=nums[i]
            maxx=max(summ,maxx)
            if summ<0:
                summ=0
        return maxx  
#Time complexity:O(N)
#Space complexity:O(1)
