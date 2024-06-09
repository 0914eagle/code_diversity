
def solve(n, p, a):
    # Calculate the number of valid permutations for each x
    f = [0] * (n + 1)
    f[0] = 1
    for i in range(1, n + 1):
        f[i] = f[i - 1] * i
    
    # Find all good integers x
    good_integers = []
    for x in range(1, n + 1):
        if f[x] % p != 0:
            good_integers.append(x)
    
    return len(good_integers), good_integers

