def is_equal_to_sum_even(n):
    
    # Your code here
    if n < 8:
        return False
    elif n == 8:
        return True
    else:
        for i in range(2, n//2):
            if is_equal_to_sum_even(n-i) == True:
                return True
        return False

