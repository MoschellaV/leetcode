class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        solutionSet = ""

        shortestString =  min(strs, key=len)
        

        for i in range(len(shortestString)):
            for string in strs:
                if string[i] != shortestString[i]:
                    return solutionSet
                
            solutionSet += shortestString[i]

        return solutionSet