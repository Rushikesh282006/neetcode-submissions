class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_prod = nums[0]
        min_prod = nums[0]
        res = nums[0]
        
        for i in range(1,len(nums)):
            n = nums[i]

            if n<0:
                max_prod, min_prod = min_prod, max_prod

            max_prod = max(max_prod*n,n)
            min_prod = min(min_prod*n,n)

            res = max(res,max_prod)

        return res
