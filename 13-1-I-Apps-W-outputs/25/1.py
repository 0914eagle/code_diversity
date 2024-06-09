
def get_max_gcd(n):
    # Initialize the maximum gcd as 1
    max_gcd = 1
    # Iterate through all pairs of integers from 1 to n
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            # Calculate the gcd of the current pair
            gcd = get_gcd(i, j)
            # Update the maximum gcd if necessary
            if gcd > max_gcd:
                max_gcd = gcd
    return max_gcd

def get_gcd(a, b):
    if b == 0:
        return a
    else:
        return get_gcd(b, a % b)

n = int(input())
print(get_max_gcd(n))

