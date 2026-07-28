class Solution:
    def findMin(self, nums: List[int]) -> int:

        l,r = 0,len(nums)-1
        min_num = float('inf')
        while l<=r:
            mid = (l+r) // 2
            if nums[mid] == -float('inf') or l==r:
                min_num = min(nums[mid],min_num)
                break
            elif nums[mid]>min_num:
                if nums[l]>min_num:
                    l = mid + 1
                else:
                    min_num = nums[l]
                    r = mid - 1
            else:
                min_num = nums[mid]
                if nums[r] > min_num:
                    r = mid-1
                else:
                    l = mid+1
        
        return min_num