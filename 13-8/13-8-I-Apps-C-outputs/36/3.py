
def find_last_digits(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    
    factorial_str = str(factorial)
    index = factorial_str.rfind('0')
    
    if index == 0:
        return '0'
    else:
        return factorial_str[index-2:index]

