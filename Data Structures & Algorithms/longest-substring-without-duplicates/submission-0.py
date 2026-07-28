class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0 or len(s)==1:
            return len(s)
            
        temp = []
        max_sub_len = 0
        for i in range(len(s)):
            if s[i] not in temp:
                temp.append(s[i])
                max_sub_len = max(max_sub_len, len(temp))
            elif s[i] in temp:
                j = 0
                while temp[j] != s[i]:
                    j += 1
                temp = temp[j+1:]
                temp.append(s[i])

        return max_sub_len
