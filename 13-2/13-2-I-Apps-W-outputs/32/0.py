
def count_ways(n, m, permutations):
    # Initialize a set to store the common parts
    common_parts = set()
    
    # Iterate over each permutation
    for permutation in permutations:
        # Iterate over each position in the permutation
        for i in range(n):
            # Check if the current position is a common part
            if all(permutation[i] in p for p in permutations):
                # Add the current position to the set of common parts
                common_parts.add(permutation[i])
    
    # Return the number of ways to delete a prefix and suffix from each permutation
    return len(common_parts)

def main():
    n, m = map(int, input().split())
    permutations = [list(map(int, input().split())) for _ in range(m)]
    print(count_ways(n, m, permutations))

if __name__ == '__main__':
    main()

