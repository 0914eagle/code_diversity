
def compute_e(n):
    result = 0
    for i in range(n+1):
        result += 1/factorial(i)
    return result

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

