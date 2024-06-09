
import math

def solve(n, a):
    # Calculate the number of possible orders
    num_orders = math.factorial(n)
    
    # Subtract the number of invalid orders
    for i in range(n):
        num_orders -= (a[i] * (n - a[i] - 1))
    
    # Return the result modulo 10^9+7
    return num_orders % 1000000007

