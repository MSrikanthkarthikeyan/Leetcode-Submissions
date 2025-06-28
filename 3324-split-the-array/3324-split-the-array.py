class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return False
        count = Counter(nums)
        for num,val in count.items():
            if val>2:
                return False
        return True        