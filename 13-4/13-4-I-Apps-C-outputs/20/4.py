
def f1(n, k, p):
    # Calculate the number of permutations of length n with runs of length at most k
    num_permutations = 1
    for i in range(1, n+1):
        num_permutations *= (k+1-i)
    num_permutations %= p
    return num_permutations

def f2(n, k, p):
    # Calculate the number of permutations of length n with runs of length at most k, using the inclusion-exclusion principle
    num_permutations = 0
    for i in range(1, k+1):
        num_permutations += f1(n, i, p)
    num_permutations %= p
    return num_permutations

if __name__ == '__main__':
    n, k, p = map(int, input().split())
    print(f2(n, k, p))

