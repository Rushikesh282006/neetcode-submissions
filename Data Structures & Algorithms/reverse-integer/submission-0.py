class Solution:
    def reverse(self, x: int) -> int:
        num = abs(x)
        rev=0
        while num!=0:
            rem = num%10
            rev = rev*10 + rem 
            num = num//10
        rev =  rev if x>0 else -1*rev
        if rev>2**31-1 or rev<-2**31:
            return 0
        return rev