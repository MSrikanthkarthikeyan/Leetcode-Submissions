class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(current):
            if current not in res:
                res.append(current)
            for i in range(len(current)):
                temp = current[:i] + current[i+1:]
                helper(temp)

        helper(nums)
        return res
