class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return 0

        s = []
        res = [0]*len(temperatures)
        prev_ind = 0

        
        for i in range(len(temperatures)):
            while len(s) != 0 and temperatures[i] > temperatures[s[-1]]:
                prev_ind = s.pop()
                res[prev_ind] = i - prev_ind
            
            s.append(i)

        return res