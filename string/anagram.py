#https://leetcode.com/problems/valid-anagram/
#one method is to sort the strings and compare.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictt=defaultdict(int)
        for x in s:
            dictt[x]+=1
        for x in t:
            dictt[x]-=1
        for val in dictt.values():
            if val!=0:
                return False
        return True
