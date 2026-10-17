class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {} #num -> count

        for n in nums:
            if n not in myDict:
                myDict[n] = 0
            else:
                myDict[n] += 1
        
        listK = sorted(myDict, key=myDict.get, reverse = True)[:k]
        return listK

        #time: O(nlogn)
        #space: O(n)