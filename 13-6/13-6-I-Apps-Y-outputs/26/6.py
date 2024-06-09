
def solve(a):
    # Find the greatest common divisor (gcd) of all elements in the array
    gcd = a[0]
    for i in range(1, len(a)):
        gcd = gcd_recursive(gcd, a[i])
    
    # Count the number of positive integers that divide gcd
    count = 0
    for i in range(1, gcd + 1):
        if gcd % i == 0:
            count += 1
    
    return count

def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)

