#https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        q=deque()
        mapp={')':'(',']':'[','}':'{'}
        for x in s:
            if x in mapp.values():
                q.append(x)
            else:
                if q and q[-1]==mapp[x]:
                    q.pop()
                else:
                    return False        
        if q:
            return False            
        return True
