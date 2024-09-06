#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        minn=float('inf')
        while low<=high:
            mid=(low+high)//2
            if nums[low]<=nums[mid]:
                minn=min(minn,nums[low]) #for special case where mid element could be the minimum also in the sorted part. eg.[4,5,1,2,3]
                low=mid+1
            else:
                minn=min(minn,nums[mid])
                high=mid-1 
        return minn           
#Time complexity:O(log(N))
#Space complexity:O(1)
