
def common_divisors(a):
    # Find the greatest common divisor (GCD) of all elements in the array
    gcd = a[0]
    for i in range(1, len(a)):
        gcd = math.gcd(gcd, a[i])
    
    # Return the number of positive integers that divide gcd
    count = 0
    for i in range(1, gcd + 1):
        if gcd % i == 0:
            count += 1
    
    return count
