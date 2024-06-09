
def common_divisors(arr):
    # Find the greatest common divisor (GCD) of all elements in the array
    gcd = arr[0]
    for i in range(1, len(arr)):
        gcd = _gcd(gcd, arr[i])
    
    # Return the number of positive integers that divide gcd
    count = 0
    for i in range(1, gcd + 1):
        if gcd % i == 0:
            count += 1
    return count

def _gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

