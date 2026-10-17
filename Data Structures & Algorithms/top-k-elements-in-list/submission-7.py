class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        listList = [[] for _ in range(len(nums) + 1)]
        count = {}

        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                listList[count[n]].remove(n)
                count[n] += 1
            listList[count[n]].append(n)

        result = []
        
        for i in range(len(nums), -1, -1):
            if k <= 0:
                break
            else:
                for x in listList[i]:
                    result.append(x)
                    k -= 1
        
        return result