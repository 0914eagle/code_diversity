
def is_equal_to_sum_even(n: int) -> bool:
    
    if n % 2 == 1:
        return False
    else:
        total = 0
        for i in range(1, int(n/2)+1):
            if i % 2 == 0:
                total += i
                if total == n:
                    return True
        return False

