
def solve(x, arr):
    # Calculate the sum of the array
    sum_arr = sum(arr)
    # Calculate the product of the array
    prod_arr = 1
    for i in arr:
        prod_arr *= i
    # Calculate the greatest common divisor of x and the product of the array
    gcd = gcd_fun(x, prod_arr)
    # Calculate the result of the fraction
    result = (sum_arr * gcd) // x
    # Return the result modulo 1000000007
    return result % 1000000007

def gcd_fun(a, b):
    if b == 0:
        return a
    else:
        return gcd_fun(b, a % b)

x = int(input())
arr = list(map(int, input().split()))
print(solve(x, arr))

