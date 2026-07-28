class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = list("".join(char for char in s if char.isalnum()).lower())
        for i in range(len(x)//2):
            front = x[i]
            rear = x[len(x)-1-i]
            if front != rear:
                return False
        return True
            