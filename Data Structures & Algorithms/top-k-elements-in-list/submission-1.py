class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #dict where key is num, value is count
        numsToCount = {}

        for num in nums:
            if num in numsToCount:
                numsToCount[num]+=1
            else:
                numsToCount[num] = 1

        #convert value to list, sort from max, keep k nums
        #find key from value that's == sorted
        
        sortedNums = sorted(numsToCount, key=lambda num: numsToCount[num], reverse=True)
        return sortedNums[:k]