import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while r > l:
            mid = (r+l) // 2
            
            hr = 0
            #loop through piles
            for pile in piles:
                hr += math.ceil(pile / mid)
            
            if hr > h:
                l =  mid + 1
            else:
                r = mid
        
        return l