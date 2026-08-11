import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1           
        r = max(piles)
        
        def check(speed, piles, h):
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / speed) 
            return total_hours <= h

        while l <= r:
            mid = (l + r) // 2
            
            if check(mid, piles, h):
                r = mid - 1
            else:
                l = mid + 1
                
        return l         