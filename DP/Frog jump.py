#https://leetcode.com/problems/jump-game/submissions/1384365384/
#greedy
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxx=0
        for i in range(len(nums)):
            if i<=maxx:
                maxx=max(maxx,i+nums[i])
            else:
                return False
        return True        


            

