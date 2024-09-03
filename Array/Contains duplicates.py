#https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count=set()
        for i in range(len(nums)):
               count.add(nums[i])
        if len(count)<len(nums):
            return True      
        return False       
#time complexity:O(n)
#space complexity worst case:O(n)
      
                  
