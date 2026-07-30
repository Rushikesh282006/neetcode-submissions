class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        s = 0
        for num in nums:
            s ^= num
        return s