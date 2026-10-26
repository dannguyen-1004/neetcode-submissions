import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []

        for i, point in enumerate(points):
            dis = (point[0] - 0)**2 + (point[1] - 0)**2
            heapq.heappush(heap, (dis, point))

            
        for r in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
        