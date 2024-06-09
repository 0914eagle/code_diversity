
def count_common_divisors(arr):
    # Find the greatest common divisor (GCD) of all elements in the array
    gcd = arr[0]
    for i in range(1, len(arr)):
        gcd = math.gcd(gcd, arr[i])
    
    # Return the number of positive integers that divide gcd
    return len([x for x in range(1, gcd + 1) if gcd % x == 0])

