
def find_trailing_zeroes(n):
    factorial = 1
    for i in range(2, n+1):
        factorial *= i
    
    while factorial % 10 == 0:
        factorial //= 10
    
    last_three_digits = str(factorial)[-3:]
    return last_three_digits

