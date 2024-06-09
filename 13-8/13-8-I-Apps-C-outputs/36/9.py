
def trailing_zeroes(n):
    count = 0
    while n % 10 == 0:
        n //= 10
        count += 1
    return count

def last_three_digits(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    factorial_str = str(factorial)
    if len(factorial_str) <= 3:
        return factorial_str
    else:
        return factorial_str[-3:]

n = int(input())
print(last_three_digits(n))

