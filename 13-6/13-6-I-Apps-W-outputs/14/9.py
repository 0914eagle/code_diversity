
def get_trailing_zeroes(m):
    count = 0
    for i in range(1, m+1):
        count += get_factorial_trailing_zeroes(i)
    return count

def get_factorial_trailing_zeroes(n):
    count = 0
    while n % 10 == 0:
        n //= 10
        count += 1
    return count

