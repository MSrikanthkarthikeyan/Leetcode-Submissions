class Solution:
    def form(self, s:str) -> str:
        alphabet_dict = {chr(i): chr(i+1) for i in range(ord('a'), ord('z')+1)}
        alphabet_dict['z'] = 'a'
        res = ""
        for i in range(len(s)):
            if s[i].lower() in alphabet_dict:
                res += alphabet_dict[s[i].lower()]
            else:
                res += s[i]
        return res        


    def kthCharacter(self, k: int) -> str:
        string="a"
        while len(string)<k:
            string+=self.form(string)
        return string[k-1]    
