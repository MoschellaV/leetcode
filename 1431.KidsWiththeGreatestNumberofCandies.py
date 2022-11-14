class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        
        solution = []
        maxCandies = max(candies)
        
        for candy in candies:
            if candy + extraCandies >= maxCandies:
                solution.append(True)
            else:
                solution.append(False)
                
        return solution
