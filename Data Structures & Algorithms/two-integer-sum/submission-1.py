class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for i, val in enumerate(nums):
            search = target - val
            if search in check:
                return [check[search], i]
            check[val] = i