class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(n+1):
            x = bin(i)[2:]
            c = Counter(x)
            res.append(c['1'])

        return res