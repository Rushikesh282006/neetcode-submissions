class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        temp = ""
        for n in digits:
            temp += str(n)

        res = int(temp) + 1
        res = str(res)
        return [res[i] for i in range(len(res))]