from typing import List

class Solution:
    def possible(self, weights: List[int], capacity: int) -> int:
        ndays = 1 
        load = 0
        for weight in weights:
            if load + weight > capacity:
                ndays += 1
                load = weight
            else:
                load += weight
        return ndays

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        while low < high:
            mid = (low + high) // 2
            ndays = self.possible(weights, mid)
            if ndays <= days:
                high = mid
            else:
                low = mid + 1 

        return low
