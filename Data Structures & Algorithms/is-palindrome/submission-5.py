class Solution:
    def isPalindrome(self, s: str) -> bool:
        news = ''
        for ch in s:
            if ch.isalnum():
                news += ch.lower() 
        if news == news[::-1]:
            return True 
        else:
            return False 
        

