
def count_permutations(n, k, p):
    # Calculate the number of permutations of length n
    num_permutations = 1
    for i in range(n):
        num_permutations = (num_permutations * (n - i)) % p
    
    # Calculate the number of permutations with runs of length k or less
    num_runs = 0
    for i in range(n - k + 1):
        # Calculate the number of runs of length k or less in the ith prefix of the permutation
        num_runs_prefix = 0
        for j in range(i + 1, n + 1):
            if j - i < k:
                num_runs_prefix += 1
            else:
                break
        num_runs += num_runs_prefix
    
    return (num_permutations - num_runs) % p

def main():
    n, k, p = map(int, input().split())
    print(count_permutations(n, k, p))

if __name__ == '__main__':
    main()

