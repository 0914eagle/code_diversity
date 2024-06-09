
def solve(n, k, p):
    # Calculate the number of permutations of length n with runs of length at most k
    num_permutations = 1
    for i in range(1, n+1):
        num_permutations *= (k+1-i)
        num_permutations %= p
    return num_permutations

