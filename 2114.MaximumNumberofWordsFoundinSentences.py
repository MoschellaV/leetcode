class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:    

        solution = 0    
    
        for sen in sentences:
            words = list(sen.split(" "))
            solution = max(solution, len(words))
        
        return solution
            