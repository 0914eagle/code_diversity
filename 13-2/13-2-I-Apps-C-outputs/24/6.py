
import math

def special_numbers(n, k):
    def count_set_bits(n):
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count
    
    def is_special(n, k):
        count = count_set_bits(n)
        return count == k
    
    def count_special_numbers(n, k):
        count = 0
        for i in range(1, n+1):
            if is_special(i, k):
                count += 1
        return count
    
    return count_special_numbers(n, k) % (10**9 + 7)

