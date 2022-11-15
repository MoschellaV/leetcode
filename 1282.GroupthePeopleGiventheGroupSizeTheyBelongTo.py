class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        
        solution = []
        
        # catch edge case
        print(len(groupSizes))
        if len(groupSizes) == 1: return [[0]]
            
        for i in range(len(groupSizes)):
           
            # get minimum number (represents the smalles array)
            minValue = min(groupSizes)
            
            #create temp array that will store index
            temp = []
            
            # to stop the function from inifinetly looping
            if (minValue == 501): return solution
            
            # iterates to store appropriate elements in appropriate length array
            for k in range(minValue):
                
                # get the index of the smallest value
                indexMinValue = groupSizes.index(minValue)
                
                # store that index
                temp.append(indexMinValue)
                

                # set that index to 501 as to not disturb
                # the index's of other elements Note* 501 is out
                # of bounds in constraints
                groupSizes[indexMinValue] = 501
                
            
            solution.append(temp)
                
        return solution