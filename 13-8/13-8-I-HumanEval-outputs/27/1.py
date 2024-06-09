
def is_equal_to_sum_even(n: int) -> bool:
    
    if n % 2 == 1:  # If n is odd, it cannot be written as the sum of even numbers
        return False
    # If n is even, we can try all combinations of 4 even numbers that add up to n
    for i in range(1, int(n/2)):
        if i**2 + (n-i**2) == n:
            return True
    return False

