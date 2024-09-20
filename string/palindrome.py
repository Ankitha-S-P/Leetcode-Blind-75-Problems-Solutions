#https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        digit=0 
        original=x   
        while x>0:
            digit=(digit*10)+x%10
            x=x//10
        if digit==original:
            return True
        return False
