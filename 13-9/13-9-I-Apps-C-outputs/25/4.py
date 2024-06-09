
def solve(n, a):
    # Check if at least one box has at least one chocolate piece
    if not any(a):
        return -1
    
    # Find the smallest positive integer that is common to all boxes
    gcd = a[0]
    for i in range(1, n):
        gcd = math.gcd(gcd, a[i])
    
    # If the GCD is 1, then there is no way to make Alice happy
    if gcd == 1:
        return -1
    
    # Calculate the minimum number of seconds needed to make Alice happy
    seconds = 0
    for i in range(n):
        seconds += a[i] // gcd
    
    return seconds

