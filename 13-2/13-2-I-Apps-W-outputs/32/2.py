
def count_ways(n, m, permutations):
    # Initialize a set to store the common prefixes and suffixes
    common_parts = set()
    
    # Iterate over each permutation
    for permutation in permutations:
        # Initialize a set to store the prefixes and suffixes of this permutation
        prefixes_and_suffixes = set()
        
        # Iterate over each element in the permutation
        for i in range(n):
            # Add the prefix of length i to the set of prefixes and suffixes
            prefixes_and_suffixes.add(permutation[:i])
            # Add the suffix of length i to the set of prefixes and suffixes
            prefixes_and_suffixes.add(permutation[i:])
        
        # Update the set of common prefixes and suffixes
        common_parts = common_parts.intersection(prefixes_and_suffixes)
    
    # Return the number of ways to delete a prefix and a suffix from each permutation
    return len(common_parts)

def main():
    n, m = map(int, input().split())
    permutations = []
    for _ in range(m):
        permutations.append(list(map(int, input().split())))
    print(count_ways(n, m, permutations))

if __name__ == '__main__':
    main()

