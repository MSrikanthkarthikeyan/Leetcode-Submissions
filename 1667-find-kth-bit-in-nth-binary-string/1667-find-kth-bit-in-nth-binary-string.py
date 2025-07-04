class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s: str) -> str:
            return ''.join('1' if c == '0' else '0' for c in s)
        
        s = "0"
        for _ in range(1, n):
            s = s + "1" + invert(s)[::-1]
        return s[k - 1]
