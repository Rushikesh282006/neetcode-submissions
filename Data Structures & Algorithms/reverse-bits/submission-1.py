class Solution:
    def reverseBits(self, n: int) -> int:
        res = ""
        str_n = bin(n)[2:].zfill(32)

        print(str_n)
        for i in range(len(str_n)):
            res += str_n[len(str_n)-1-i] 

        return int(res,2)