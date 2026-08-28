class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        max_num = max(nums)

        for i in range(max_num+1):
            if i not in set(nums):
                return i
        
        return max_num+1