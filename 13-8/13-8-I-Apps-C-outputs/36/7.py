
def find_trailing_zeroes(n):
    factorial = 1
    for i in range(2, n+1):
        factorial *= i
    
    trailing_zeroes = 0
    while factorial % 10 == 0:
        trailing_zeroes += 1
        factorial //= 10
    
    last_three_digits = str(factorial)[:3]
    return last_three_digits

