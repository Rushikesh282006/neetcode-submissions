class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(0,len(nums)-1):
            slow = nums[i]
            fast = nums[i+1]
            if slow==fast:
                return True
        return False
