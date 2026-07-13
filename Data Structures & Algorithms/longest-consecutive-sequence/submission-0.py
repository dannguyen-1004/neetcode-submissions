class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numsSet = set(nums)
        numsDict = {}

        for num in numsSet:
            self.findLength(num, numsSet, numsDict)

        return max(numsDict.values())

    def findLength(self, num, numsSet, numsDict):
        if num in numsDict:
            return numsDict[num]

        if num - 1 in numsSet:
            numsDict[num] = 1 + self.findLength(
                num - 1,
                numsSet,
                numsDict
            )
        else:
            numsDict[num] = 1

        return numsDict[num]