
def solve(n, p, a):
    # Initialize a list to store the number of valid permutations for each x
    f = [0] * (n + 1)
    f[0] = 1
    for i in range(1, n + 1):
        # Calculate the number of valid permutations for x = i
        f[i] = f[i - 1] * (n - i + 1)
        for j in range(1, i):
            if a[j] % i == 0:
                f[i] -= f[i - j]
        f[i] = f[i] % (p - 1)
    # Return the number of good integers
    return sum(f[i] for i in range(1, n + 1) if f[i] % p != 0)

