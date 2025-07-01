class Solution:
    def possibleStringCount(self, word: str) -> int:
        res=1
        for i in range(len(word)-1):
            if word[i]==word[i+1]:
                res+=1
            else:
                res+=0
        return res            






        # res=1
        # count=Counter(word)
        # for num,val in count.items():
        #     if val>1:
        #         res+=val-1
        # return res        

