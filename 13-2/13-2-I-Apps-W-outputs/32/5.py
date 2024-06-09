
def count_ways(n, m, permutations):
    # Initialize a set to store the common parts
    common_parts = set()
    
    # Iterate over each permutation
    for permutation in permutations:
        # Initialize a set to store the current part
        current_part = set()
        
        # Iterate over each element in the permutation
        for element in permutation:
            # If the element is not in the current part, add it
            if element not in current_part:
                current_part.add(element)
            # If the element is already in the current part, remove it
            else:
                current_part.remove(element)
        
        # Add the current part to the common parts set
        common_parts.add(current_part)
    
    # Return the number of ways to delete a prefix and a suffix
    return len(common_parts)

def main():
    n, m = map(int, input().split())
    permutations = []
    for _ in range(m):
        permutations.append(list(map(int, input().split())))
    print(count_ways(n, m, permutations))

if __name__ == '__main__':
    main()

