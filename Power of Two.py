class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        # Power of 2 numbers, cannot be 0 or negative
        if n <= 0:
            return False

        # Keep dividing by 2 until number becomes odd
        while n % 2 == 0:
            n //= 2

        # If final number becomes 1,
        # it means n was completely divisible by 2
        if n == 1:
            return True
        else:
            return False
