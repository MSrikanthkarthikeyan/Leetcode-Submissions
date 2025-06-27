class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = []
        i = 1  # Start from 1, not 0
        idx = 0

        while len(missing) < k:
            if idx < len(arr) and arr[idx] == i:
                idx += 1
            else:
                missing.append(i)
            i += 1

        return missing[-1]
