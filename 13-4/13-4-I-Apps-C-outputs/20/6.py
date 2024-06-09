
def count_permutations(n, k, p):
    # Initialize the number of permutations to 1
    num_permutations = 1
    
    # Iterate over the length of the permutation
    for i in range(n):
        # Calculate the number of permutations with a run of length i
        num_permutations *= (k - i) * (n - i)
        num_permutations %= p
    
    return num_permutations

def main():
    n, k, p = map(int, input().split())
    print(count_permutations(n, k, p))

if __name__ == '__main__':
    main()

