
def solve(a):
    # Find the greatest common divisor (gcd) of all elements in the array
    gcd = a[0]
    for i in range(1, len(a)):
        gcd = gcd_two_numbers(gcd, a[i])
    
    # Count the number of positive integers x that divide each number in the array
    count = 0
    for i in range(1, gcd + 1):
        if gcd % i == 0:
            count += 1
    
    return count

def gcd_two_numbers(a, b):
    if b == 0:
        return a
    else:
        return gcd_two_numbers(b, a % b)

