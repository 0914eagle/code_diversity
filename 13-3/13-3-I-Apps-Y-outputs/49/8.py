
import math

def solve(n, a):
    # Calculate the number of possible orders
    num_orders = math.factorial(n)
    
    # Subtract the number of invalid orders
    for i in range(n):
        num_orders -= math.factorial(a[i])
    
    return num_orders % (10**9 + 7)

