class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        l=[]
        count=Counter(nums)
        for num,val in count.items():
            if val>1:
                l.append(num)
        return l        