class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        l = []
        word = ""
        i = 0
        while i < len(s):
            if s[i] != " ":
                word += s[i]
            else:
                if word:  
                    l.append(word)
                    word = ""
            
                while i < len(s) and s[i] == " ":
                    i += 1
                continue  
            i += 1
        if word:
            l.append(word)

        l.reverse()
        return " ".join(l)
