class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        xReversed = str(x)[::-1]
        
        if str(x) == str(xReversed): return True
         
        else: return False

