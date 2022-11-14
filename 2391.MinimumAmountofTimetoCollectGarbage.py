class Solution:
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        
        solution = 0
        
        maxIndexM = 0
        maxIndexP = 0
        maxIndexG = 0
        
        # detect last iterations
        for i in range(len(garbage)):
            # print(i)
            
            if "M" in garbage[i]:
                maxIndexM = i
                
            if "P" in garbage[i]:
                maxIndexP = i
                
            if "G" in garbage[i]:
                maxIndexG = i
                
        # summation of max turck movement
        for i in range(maxIndexM):
            solution += travel[i]
        for i in range(maxIndexP):
            solution += travel[i]
        for i in range(maxIndexG):
            solution += travel[i]
        
        # sum of all garbage
        for i in range(len(garbage)):
            solution += len(garbage[i])
            
        return solution
            
            
            
                
            
            
            
            