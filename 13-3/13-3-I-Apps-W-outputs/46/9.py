
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def solve(n, x, arr):
    numerator = 0
    denominator = 0
    for i in range(n):
        numerator += 1 / (x ** arr[i])
        denominator += arr[i]
    gcd_value = gcd(numerator, denominator)
    return numerator // gcd_value % 1000000007

