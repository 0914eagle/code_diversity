
def is_equal_to_sum_even(n: int) -> bool:
    
    if n % 2 == 1:
        return False
    else:
        sum_even = 0
        for i in range(1, int(n/2)+1):
            if i % 2 == 0:
                sum_even += i
        if sum_even == n:
            return True
        else:
            return False
