class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #dict where key is num, value is count
        numsToCount = {}

        for num in nums:
            if num in numsToCount:
                numsToCount[num]+=1
            else:
                numsToCount[num] = 1

        #sort nums by key value from max
        #return k nums
        
        sortedNums = sorted(numsToCount, key=lambda num: numsToCount[num], reverse=True)
        return sortedNums[:k]