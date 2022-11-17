class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:

        myDict = {"ele0": 0, "ele1":0, "ele2":0,"ele3":0}
        
        for i in range(4):
            if i < 2:
                myDict["ele"+str(i)] = max(nums)
            else:
                myDict["ele"+str(i)] = min(nums)
                
            nums.pop(nums.index(myDict["ele"+str(i)]))
        
        return (myDict["ele0"]*myDict["ele1"]) - (myDict["ele2"]*myDict["ele3"])