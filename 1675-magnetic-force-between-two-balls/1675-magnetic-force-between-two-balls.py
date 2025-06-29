from typing import List

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def is_valid(distance):
            count = 1
            last_pos = position[0]
            for i in range(1, len(position)):
                if position[i] - last_pos >= distance:
                    count += 1
                    last_pos = position[i]
                if count >= m:
                    return True
            return False

        low, high = 1, position[-1] - position[0]

        while low < high:
            mid = (low + high + 1) // 2  # upper mid to avoid infinite loop
            if is_valid(mid):
                low = mid  # try a bigger distance
            else:
                high = mid - 1  # try a smaller distance

        return low
