class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #graph with sorted str as key
        #value as str
        sortedToStrs = {}

        for str in strs:
            sortedStr = "".join(sorted(str))
            if sortedStr in sortedToStrs:
                sortedToStrs[sortedStr].append(str)
            else:
                sortedToStrs[sortedStr] = [str]
        
        return list(sortedToStrs.values())