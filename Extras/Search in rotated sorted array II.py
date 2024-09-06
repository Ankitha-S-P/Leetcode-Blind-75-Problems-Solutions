#https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return True
                #if low,mid,high value is same , the normal algo for this kinda problem wont work.....since target!=nums[mid] already...
                #we can eliminate low and high index values obviously...then continue again
            if nums[low]==nums[mid] and nums[high]==nums[mid]:
                low+=1
                high-=1
                continue
            if nums[low]<=nums[mid]:
                if target>=nums[low] and target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if target>nums[mid] and target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1                   
        return False

  #Time complexity:O(log(N))
  #Space complexity:O(1)
