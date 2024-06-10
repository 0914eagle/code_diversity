
def is_equal_to_sum_even(n: int) -> bool:
    
    if n % 2 != 0:
        return False
    else:
        n //= 2
        i = 1
        while i <= 4:
            if n < i * 2:
                return False
            n -= i * 2
            i += 1
        return True

