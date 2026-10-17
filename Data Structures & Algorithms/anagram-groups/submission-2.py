class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def convertStringToTuple(s: str):
            listStr = [0] * 26
            for i, n in enumerate(s):
                listStr[ord(n) - ord('a')] += 1
            return tuple(listStr)

        dictWords = {}

        for stri in strs:
            converted = convertStringToTuple(stri)
            
            if converted in dictWords:
                dictWords[converted].append(stri)
            else:
                dictWords[converted] = [stri]
        
        return list(dictWords.values())
            