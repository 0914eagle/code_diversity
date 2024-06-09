
def divisibility_hack(b, d):
    # Check if d is a prime number
    if d == 1:
        return "no"
    
    # Iterate through possible values of m
    for m in range(1, b):
        # Calculate the reduction function for m
        f = lambda n: (n // b**m) * b**m + sum(int(n % b**i / b**(i-m)) for i in range(m, 0, -1))
        
        # Check if f(b**k) is divisible by d for all k
        for k in range(1, b):
            if f(b**k) % d != 0:
                break
        else:
            return "yes"
    
    return "no"

