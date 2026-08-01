class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = {1:1,2:2,3:3}


        def find_steps(x):
            if x in cache:
                return cache[x]
            else:
                cache[x] = find_steps(x-1) + find_steps(x-2)
                return cache[x]
            
        return find_steps(n)