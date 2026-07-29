class Solution:

    def encode(self, strs: List[str]) -> str:

        enc_str = ""

        for s in strs:
            if len(s)>9 and len(s)<100:
                enc_str += '*' + str(len(s)) + s
            elif len(s)>99:
                enc_str += '#' + str(len(s)) + s
            else:
                enc_str += str(len(s)) + s

        return enc_str

    def decode(self, s: str) -> List[str]:

        res = []

        i=0

        while i < len(s):
            if s[i] == '*':
                str_len = int(s[i+1:i+3])
                i += 2
            elif s[i] == '#':
                str_len = int(s[i+1:i+4])
                i += 3
            else:
                str_len = int(s[i])
                
            res.append(str(s[i+1:i+str_len+1]))
            i += str_len+1
                
        return res

