#https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=i
        mapp={}
        count=0
        maxx=0
        while i<len(s) and j<len(s):
            if s[j] in mapp and mapp[s[j]]>=i:
                i=mapp[s[j]]+1 
            maxx=max(maxx,j-i+1)    
            mapp[s[j]]=j
            j+=1             
        return maxx 
