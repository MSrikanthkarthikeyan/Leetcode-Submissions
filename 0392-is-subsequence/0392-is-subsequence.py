class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        k = [-1]
        l = 0
        t_index = -1

        for i in s:
            found = False
            for j in range(t_index + 1, len(t)):
                if t[j] == i:
                    t_index = j
                    k.append(j)
                    l += 1
                    found = True
                    break
            if not found:
                return False

        return l == len(s)
