class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_frequent_char_count = 0
        left = 0
        max_sub_len = 0
        
        for right in range(len(s)):

            count[s[right]] = count.get(s[right], 0) + 1
            
            max_frequent_char_count = max(max_frequent_char_count, count[s[right]])
            
            if (right - left + 1) -max_frequent_char_count > k:
                # The window is invalid, shrink it from the left
                count[s[left]] -= 1
                left += 1
                
            max_sub_len = max(max_sub_len, right - left + 1)
            
        return max_sub_len