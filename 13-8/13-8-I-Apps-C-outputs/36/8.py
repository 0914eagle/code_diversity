
def find_last_three_digits(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    
    factorial_str = str(factorial)
    zeroes = 0
    for i in range(len(factorial_str)-1, -1, -1):
        if factorial_str[i] == '0':
            zeroes += 1
        else:
            break
    
    if zeroes < 3:
        return factorial_str[:zeroes]
    else:
        return factorial_str[-3:]

