
def find_last_digits(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    
    factorial_str = str(factorial)
    for i in range(len(factorial_str)-1, -1, -1):
        if factorial_str[i] == '0':
            continue
        else:
            return factorial_str[i-2:i+1]

