class Solution:
    def minimumSum(self, num: int) -> int:
        
        newNum = list(str(num))
        newNum.sort()
        
        return int(newNum[0]+newNum[2]) + int(newNum[1]+newNum[3])
            
