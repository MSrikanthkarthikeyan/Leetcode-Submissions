class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['A','a','e','E','i','I','O','o','U','u']
        s_list = list(s)
        l = []

        # Step 1: Collect all vowels
        for ch in s_list:
            if ch in vowels:
                l.append(ch)

        # Step 2: Replace vowels in reverse order
        j = len(l) - 1
        for i in range(len(s_list)):
            if s_list[i] in vowels:
                s_list[i] = l[j]
                j -= 1

        return ''.join(s_list)
