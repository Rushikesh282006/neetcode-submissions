class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        i,j = 0,len(heights)-1

        while i<j:

            l = heights[i]
            r = heights[j]

            curr_area = l*(j-i) if l<r else r*(j-i)

            max_area = max(max_area,curr_area)

            if l<r:
                i+=1
            else:
                j-=1

        return max_area