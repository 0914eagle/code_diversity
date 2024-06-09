
def euler_approximation(n):
    result = 0
    for i in range(n):
        result += 1 / factorial(i)
    return result

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

