class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        def makeDict(s: str):
            charDict = {}

            for char in s:
                if char not in charDict:
                    charDict[char] = 1
                else:
                    charDict[char] += 1
            
            return charDict
        
        return makeDict(s) == makeDict(t)

    