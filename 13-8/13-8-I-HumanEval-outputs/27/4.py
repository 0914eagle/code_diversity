
def is_equal_to_sum_even(n: int) -> bool:
    
    if n < 4:
        return False
    elif n % 2 != 0:
        return False
    else:
        count = 0
        i = 2
        while i <= n // 2:
            if n - i >= i and (n - i) % 2 == 0:
                count += 1
                i += 1
            else:
                break
        return count == 3

