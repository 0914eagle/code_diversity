
def solve(n, k, A, B):
    # Calculate the greatest common divisor (gcd) of n and k
    gcd = _gcd(n, k)
    # If the gcd is 1, then n is already equal to 1 and we don't need to do any operations
    if gcd == 1:
        return 0
    # Initialize the minimum cost to infinity
    min_cost = float('inf')
    # Iterate through all possible values of x
    for x in range(1, n+1):
        # If x is divisible by gcd, we can divide it by gcd to get a smaller value
        if x % gcd == 0:
            # Calculate the cost of dividing x by gcd and subtracting 1 from the result
            cost = B + solve(x//gcd-1, k, A, B)
            # Update the minimum cost if the current cost is less than the previous minimum cost
            min_cost = min(min_cost, cost)
    # Return the minimum cost
    return min_cost

def _gcd(a, b):
    # Base case: if b is 0, the gcd is a
    if b == 0:
        return a
    # Recursive case: calculate the gcd of b and the remainder of a divided by b
    return _gcd(b, a%b)

