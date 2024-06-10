
def is_equal_to_sum_even(n: int) -> bool:
    
    if n % 2 != 0:
        return False
    n //= 2
    return n == sum(i for i in range(2, n+1, 2) if n % i == 0)

