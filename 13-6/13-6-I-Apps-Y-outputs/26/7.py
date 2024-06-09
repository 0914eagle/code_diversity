
def get_common_divisors(arr):
    # Find the greatest common divisor (GCD) of all elements in the array
    gcd = arr[0]
    for i in range(1, len(arr)):
        gcd = get_gcd(gcd, arr[i])
    
    # Return the number of positive integers that divide gcd
    count = 0
    for i in range(1, gcd + 1):
        if gcd % i == 0:
            count += 1
    
    return count

def get_gcd(a, b):
    if b == 0:
        return a
    else:
        return get_gcd(b, a % b)

