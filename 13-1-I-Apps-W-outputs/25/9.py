
def get_max_gcd(n):
    # Initialize the maximum gcd as 1
    max_gcd = 1
    # Iterate from 2 to n
    for i in range(2, n + 1):
        # Check if i is a divisor of n
        if n % i == 0:
            # Update the maximum gcd
            max_gcd = i
    return max_gcd

