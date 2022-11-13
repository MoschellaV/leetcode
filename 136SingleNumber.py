class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        
        sum = 0
        for num in nums:
            sum = num ^ sum
        return sum
      