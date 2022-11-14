class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        t = list(t)
        
        for char in s:
            if char in t:
                t.remove(char)
                
        return t[0]