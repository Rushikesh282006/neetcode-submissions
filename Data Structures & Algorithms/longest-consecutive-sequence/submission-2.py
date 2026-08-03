class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        temp = set(nums)
        max_len = 1
        curr_len = 0
        for n in temp:
            if n-1 not in temp:
                curr_len = 1
                while (n+curr_len) in temp:
                    curr_len += 1
                max_len = max(max_len,curr_len)
            
        return max_len
