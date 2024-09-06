#https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, h: List[int]) -> int:
        n=len(h)
        i=0
        j=n-1
        maxvol=0
        while i<j:
            if h[i]<=h[j]:
                maxvol=max(maxvol,h[i]*(j-i))
                i+=1
            else:
                maxvol=max(maxvol,h[j]*(j-i))
                j-=1
        return maxvol 
#Time complexity:O(N)
#Space complexity:O(1)
      
