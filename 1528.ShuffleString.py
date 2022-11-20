class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        
        solution = []
        
        for i in range(len(s)):
            
            currMin = indices.index(min(indices))
            
            solution.append(s[currMin])
            
            indices[currMin] = 101
            
        return ''.join(solution)