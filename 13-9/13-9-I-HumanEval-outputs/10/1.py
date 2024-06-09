
def is_equal_to_sum_even(n: int) -> bool:
    
    if n < 4:
        return False
    if n % 2 != 0:
        return False
    sum_even = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            sum_even += i
            if sum_even > n:
                return False
    return sum_even == n
