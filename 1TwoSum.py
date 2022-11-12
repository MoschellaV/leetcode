class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        map = {}
        
        for i, n in enumerate(nums):
            x = target - n
            if x in map:
                return [map[x], i]
            map[n] = i