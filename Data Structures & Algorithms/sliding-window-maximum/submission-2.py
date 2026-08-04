class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        if k == len(nums):
            return [max(nums)]

        res = []
        i = 0

        while i<len(nums)-k+1:
            temp = nums[i:i+k]
            res.append(max(temp))
            i+=1

        return res