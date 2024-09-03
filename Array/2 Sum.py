#https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n={}
        for i in range(len(nums)):
            if target-nums[i] in n:
                return [i,n[target-nums[i]]]
            else:
                n[nums[i]]=i    
#using hashing
#time complexity:O(n)
#space complexity worst case:O(n)
