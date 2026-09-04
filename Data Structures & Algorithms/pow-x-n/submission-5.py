class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Handle negative exponents by inverting x and making n positive
        if n < 0:
            x = 1 / x
            n = -n
            
        res = 1.0
        
        while n > 0:
            # If n is odd, multiply the current x into our result
            if n % 2 == 1:
                res *= x
            
            # Square the base and halve the exponent for the next iteration
            x *= x
            n //= 2
            
        return res