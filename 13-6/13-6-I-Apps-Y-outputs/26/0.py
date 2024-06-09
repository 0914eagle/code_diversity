
def solve(a):
    # Find the greatest common divisor (GCD) of all elements in the array
    gcd = a[0]
    for i in range(1, len(a)):
        gcd = gcd(gcd, a[i])
    
    # Count the number of positive integers that divide each element in the array
    count = 0
    for i in range(1, gcd + 1):
        if gcd % i == 0:
            count += 1
    
    return count
