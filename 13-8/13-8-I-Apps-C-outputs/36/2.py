
def find_trailing_zeroes(n):
    factorial = 1
    for i in range(2, n+1):
        factorial *= i
    
    count = 0
    while factorial % 10 == 0:
        count += 1
        factorial //= 10
    
    if count == 0:
        return str(factorial)[:3]
    else:
        return str(factorial)[:count+3]

