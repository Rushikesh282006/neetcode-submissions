class Solution:
    def isPalindrome(self, s: str) -> bool:
        front,rear = 0,len(s)-1

        while front<rear:
            if not s[front].isalnum():
                front +=1
            elif not s[rear].isalnum():
                rear -=1 
            else:
                if s[front].lower() != s[rear].lower():
                    return False
                front += 1
                rear -=1
        return True