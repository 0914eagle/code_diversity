
def get_cyclic_permutations(n):
    # Initialize a list to store the cyclic permutations
    cyclic_permutations = []
    
    # Iterate over all possible permutations
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                # Check if the current permutation is cyclic
                if i < j < k and permutation[i] > permutation[j] > permutation[k]:
                    # If it is, add it to the list of cyclic permutations
                    cyclic_permutations.append(permutation)
                    break
    
    # Return the number of cyclic permutations modulo 10^9 + 7
    return len(cyclic_permutations) % (10**9 + 7)

if __name__ == '__main__':
    n = int(input())
    print(get_cyclic_permutations(n))

