
import math

def solve(n, k):
    def count_bits(n):
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count
    
    def is_special(n):
        return count_bits(n) == k
    
    def count_special(n):
        count = 0
        for i in range(1, n+1):
            if is_special(i):
                count += 1
        return count
    
    return count_special(n) % (10**9 + 7)

