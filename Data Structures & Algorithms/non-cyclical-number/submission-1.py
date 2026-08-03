class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n!=1:
            
            n=self.process(n)
            if n in seen:
                return False
            seen.add(n)
            
        return True


    def process(self,num):
        new_num = 0

        while num!=0:
            new_num += (num % 10) ** 2
            num = num // 10

        return new_num