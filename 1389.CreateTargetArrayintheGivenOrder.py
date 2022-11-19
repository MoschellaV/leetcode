class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
       
        target = []
        
        [target.insert(index[i], nums[i]) for i in range(len(nums))]
            
        return target