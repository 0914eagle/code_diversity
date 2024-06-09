
def compute_e(n):
    result = 0
    for i in range(n+1):
        result += 1/math.factorial(i)
    return result

