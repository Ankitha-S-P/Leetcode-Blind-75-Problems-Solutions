#https://leetcode.com/problems/3sum/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        n=len(nums)
        for i in range(n):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=n-1  
            while j<k:  
                summ=nums[i]+nums[j]+nums[k]
                if summ==0:
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                          j+=1
                    while j<k and nums[k]==nums[k+1]:
                         k-=1
                elif summ<0:
                     j+=1
                else:
                     k-=1
        return ans                            

#Time complexity:O(Nlog(N))+O(N^2) //sorting + (for loop * while)
#Space complexity:O(1)  //excluding ans list
