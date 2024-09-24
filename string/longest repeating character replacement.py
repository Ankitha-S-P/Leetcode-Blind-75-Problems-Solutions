#https://leetcode.com/problems/longest-repeating-character-replacement/
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq=0
        mapp=defaultdict(int)
        maxlen=0
        i=0
        j=0
        while j<len(s):
            mapp[s[j]]+=1
            freq=max(freq,mapp[s[j]])
            if (j-i+1)-freq<=k:
                maxlen=max(maxlen,j-i+1)
            else:
                mapp[s[i]]-=1
                i+=1                   
            j+=1        
        return maxlen 
