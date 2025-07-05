class Solution:
    def findLucky(self, arr: List[int]) -> int:
        l=[]
        count = Counter(arr)
        for num,val in count.items():
            if num==val:
                l.append(num)
        if len(l)==0:
            return -1
        else:
            return max(l)            