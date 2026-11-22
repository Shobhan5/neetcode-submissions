class Solution:
    def isPalindrome(self, s: str) -> bool:
        news = ''
        for ch in s:
            if ch.isalnum():
                news += ch.lower() 
        return news == news[::-1]
        

