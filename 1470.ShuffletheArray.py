class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        
        solution = []
        
        for i in range(n):

            solution.append(nums[i])
            solution.append(nums[i+n])
            
        return solution
                
                