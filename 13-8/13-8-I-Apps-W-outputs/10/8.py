
def solve(n, k, A, B):
    # Calculate the greatest common divisor of n and k
    gcd = _gcd(n, k)
    
    # If the gcd is 1, then n is already equal to 1 and we don't need to do any operations
    if gcd == 1:
        return 0
    
    # Initialize the minimum number of coins to pay as 0
    min_coins = 0
    
    # While the gcd is greater than 1, perform the following operations:
    while gcd > 1:
        # If n is divisible by k, divide n by k and add the cost of division to the minimum number of coins to pay
        if n % k == 0:
            n //= k
            min_coins += B
        # Otherwise, subtract 1 from n and add the cost of subtraction to the minimum number of coins to pay
        else:
            n -= 1
            min_coins += A
        
        # Calculate the new gcd of n and k
        gcd = _gcd(n, k)
    
    # Return the minimum number of coins to pay
    return min_coins

def _gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

