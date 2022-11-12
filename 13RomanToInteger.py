class Solution:
    def romanToInt(self, s: str) -> int:
        
        romanNumerals = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        
        sum = 0
        
        for i in range(len(s)):
            if i + 1 < len(s) and romanNumerals[s[i]] <romanNumerals[s[i+1]]:
                sum -= romanNumerals[s[i]]
            else:
                sum += romanNumerals[s[i]]
                
        return sum