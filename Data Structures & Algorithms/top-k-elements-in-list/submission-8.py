class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        listList = [[] for _ in range(len(nums) + 1)]
        count = {}

        #build freq
        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1

        #build bucket
        for (key, val) in count.items():
            listList[val].append(key)

        #return kth
        result = []
        for i in range(len(nums), -1, -1):
            if k <= 0:
                break
            else:
                for x in listList[i]:
                    result.append(x)
                    k -= 1
        
        return result