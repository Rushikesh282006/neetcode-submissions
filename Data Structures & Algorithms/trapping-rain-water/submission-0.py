class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        temp = 0
        i,j = 0,1

        while j<len(height):
            if height[i] == 0:
                i+=1
                j+=1
            elif height[i] <= height[j]:
                total_water += (height[i] * (j-i-1)) - temp
                temp = 0
                i, j = j , j+1
            else:
                temp += height[j]
                j+=1
                
        if i < len(height) - 1:
            right_i = len(height) - 1
            right_j = right_i - 1
            temp = 0
            
            while right_j >= i:
                if height[right_i] <= height[right_j]:
                    total_water += (height[right_i] * (right_i - right_j - 1)) - temp
                    temp = 0
                    right_i, right_j = right_j, right_j - 1
                else:
                    temp += height[right_j]
                    right_j -= 1
                    

        return total_water