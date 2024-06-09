
def solve(a):
    # Calculate the greatest common divisor (GCD) of all elements in the array
    gcd = a[0]
    for i in range(1, len(a)):
        gcd = gcd_of_two_numbers(gcd, a[i])
    
    # Return the number of positive integers that divide gcd
    count = 0
    for i in range(1, gcd + 1):
        if gcd % i == 0:
            count += 1
    return count

def gcd_of_two_numbers(x, y):
    if y == 0:
        return x
    else:
        return gcd_of_two_numbers(y, x % y)

