
def get_last_three_digits(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    
    factorial_str = str(factorial)
    index = len(factorial_str) - 1
    last_three_digits = ""
    while index >= 0 and len(last_three_digits) < 3:
        last_three_digits = factorial_str[index] + last_three_digits
        index -= 1
    
    return last_three_digits

