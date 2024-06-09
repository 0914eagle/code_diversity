
def f1(n, k, p):
    # Calculate the number of permutations of length n with runs of length at most k
    num_permutations = 1
    for i in range(1, n+1):
        num_permutations = (num_permutations * i) % p
    num_permutations_with_runs = num_permutations
    for i in range(1, k+1):
        num_permutations_with_runs = (num_permutations_with_runs * (n-i+1)) % p
    return num_permutations_with_runs

def f2(n, k, p):
    # Calculate the number of permutations of length n with runs of length exactly k
    num_permutations = 1
    for i in range(1, n-k+1):
        num_permutations = (num_permutations * i) % p
    return num_permutations

if __name__ == '__main__':
    n, k, p = map(int, input().split())
    print(f1(n, k, p))

