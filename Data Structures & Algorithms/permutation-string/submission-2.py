class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        win_size = len(s1)
        
        if win_size > len(s2):
            return False
            
        s1_counts = Counter(s1)
        window_counts = Counter(s2[:win_size])

        
        if s1_counts == window_counts:
            return True
        
        for i in range(win_size, len(s2)):
            window_counts[s2[i]] += 1

            left_char = s2[i - win_size]
            window_counts[left_char] -= 1
            
            if window_counts[left_char] == 0:
                del window_counts[left_char]
                
            if s1_counts == window_counts:
                return True

        return False