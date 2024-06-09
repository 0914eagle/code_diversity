
def f1(n, k, p):
    # Calculate the number of permutations of length n
    num_permutations = 1
    for i in range(n):
        num_permutations = (num_permutations * (n - i)) % p
    
    # Calculate the number of permutations with runs of length k or less
    num_runs = 0
    for i in range(n - k + 1):
        num_runs += 1
    
    # Calculate the number of permutations with runs of length k or less and no runs of length k + 1 or more
    num_permutations_with_runs = 0
    for i in range(n - k + 1):
        num_permutations_with_runs += num_permutations // (k + 1)
    
    # Calculate the number of permutations with runs of length k or less and no runs of length k + 1 or more, modulo p
    return (num_permutations_with_runs * num_runs) % p

def f2(n, k, p):
    # Calculate the number of permutations of length n
    num_permutations = 1
    for i in range(n):
        num_permutations = (num_permutations * (n - i)) % p
    
    # Calculate the number of permutations with runs of length k or less
    num_runs = 0
    for i in range(n - k + 1):
        num_runs += 1
    
    # Calculate the number of permutations with runs of length k or less and no runs of length k + 1 or more
    num_permutations_with_runs = 0
    for i in range(n - k + 1):
        num_permutations_with_runs += num_permutations // (k + 1)
    
    # Calculate the number of permutations with runs of length k or less and no runs of length k + 1 or more, modulo p
    return (num_permutations_with_runs * num_runs) % p

if __name__ == '__main__':
    n, k, p = map(int, input().split())
    print(f1(n, k, p))
    print(f2(n, k, p))

