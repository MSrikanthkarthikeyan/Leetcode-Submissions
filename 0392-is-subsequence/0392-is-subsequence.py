class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        i = 0  
        for ch in t:
            if i < len(s) and ch == s[i]:
                i += 1
        return i == len(s)
