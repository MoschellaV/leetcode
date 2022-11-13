class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        
        solution = []
        
        for i in range(len(nums)):
            
            current = 0
            
            for k in range(i+1):
                
                current += nums[k]
            
            solution.append(current)

        return solution
