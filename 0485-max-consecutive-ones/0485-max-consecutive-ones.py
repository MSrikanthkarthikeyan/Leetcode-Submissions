class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=0
        maximum=0
        for i in range(len(nums)):
            if nums[i]==1:
                l+=1
                if l>maximum:
                    maximum=l
            else:
                l=0
        return maximum                