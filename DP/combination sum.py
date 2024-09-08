#https://leetcode.com/problems/combination-sum/
#recursive
class Solution:
    def combinationSum(self, c: List[int], target: int) -> List[List[int]]:
        def f(n,target):
            if n==len(c):
                if target==0:
                    ans.append(combi.copy())
                return            
            f(n+1,target) #notake
            if c[n]<=target:  #take
                combi.append(c[n])
                f(n,target-c[n]) 
                combi.pop() #backtrack as we should give back the combi without any changes
        combi=[]
        ans=[]       
        f(0,target)
        return ans
