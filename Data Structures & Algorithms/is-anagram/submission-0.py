class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        res=[]
        for i in s:
            res.append(i)
        try:
            for j in t:
                res.remove(j)
            return True
        except ValueError:
            return False