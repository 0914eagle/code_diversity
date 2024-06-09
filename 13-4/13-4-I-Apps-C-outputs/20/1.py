
def f1(n, k, p):
    # Calculate the number of permutations of length n with runs of length at most k
    num_permutations = 1
    for i in range(1, n+1):
        num_permutations *= i
    num_permutations //= k+1
    
    # Calculate the number of permutations with runs of length k+1 or more
    num_runs = 0
    for i in range(1, n-k):
        num_runs += (n-i) * (n-i-1) // 2
    num_permutations -= num_runs
    
    # Return the result modulo p
    return num_permutations % p

def f2(n, k, p):
    # Calculate the number of permutations of length n with runs of length at most k
    num_permutations = 1
    for i in range(1, n+1):
        num_permutations *= i
    num_permutations //= k+1
    
    # Calculate the number of permutations with runs of length k+1 or more
    num_runs = 0
    for i in range(1, n-k):
        num_runs += (n-i) * (n-i-1) // 2
    num_permutations -= num_runs
    
    # Return the result modulo p
    return num_permutations % p

if __name__ == '__main__':
    n, k, p = map(int, input().split())
    print(f1(n, k, p))
    print(f2(n, k, p))

