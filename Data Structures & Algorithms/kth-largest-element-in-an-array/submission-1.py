class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)-1
        return nums[n-k+1]