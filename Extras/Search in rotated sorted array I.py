#https://leetcode.com/problems/search-in-rotated-sorted-array/description/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            if nums[low]<=nums[mid]:
                if target>=nums[low] and target<nums[mid]:
                    high=mid-1 
                else:
                    low=mid+1       
            else:
                if target<=nums[high] and target>nums[mid]:
                    low=mid+1
                else:
                    high=mid-1    
        
        return -1

  #Time complexity:O(log(N))
  #Space complexity:O(1)
