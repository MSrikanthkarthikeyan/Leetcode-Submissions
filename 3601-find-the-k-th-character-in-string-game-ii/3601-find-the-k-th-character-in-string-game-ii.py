class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        def shift(c):
            return chr(((ord(c) - ord('a') + 1) % 26) + ord('a'))

        stack = [] 
        n = len(operations)
        while n > 0:
            n -= 1
            half = 2 ** n
            if k > half:
                k -= half
                stack.append(operations[n])
            else:
                stack.append(0)

        c = 'a'
        for op in reversed(stack):
            if op == 1:
                c = shift(c)
        return c
