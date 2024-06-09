
def get_zeroes_in_factorial(m):
    count = 0
    for i in range(1, 100001):
        factorial = 1
        for j in range(1, i+1):
            factorial *= j
        if str(factorial).endswith(str(0) * m):
            count += 1
    return count

