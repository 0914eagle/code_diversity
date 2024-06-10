
def get_permutation_swaps(permutation, allowed_swaps):
    
    # Initialize a dictionary to keep track of the number of swaps required for each element
    swaps = {i: 0 for i in range(1, len(permutation) + 1)}

    # Loop through the allowed swaps and update the dictionary
    for a, b in allowed_swaps:
        swaps[a] += 1
        swaps[b] += 1

    # Return the maximum number of swaps required for any element
    return max(swaps.values())

def get_permutation_from_swaps(permutation, swaps):
    
    # Create a copy of the initial permutation
    result = permutation[:]

    # Loop through the swaps and apply them to the result
    for a, b in swaps:
        result[a - 1], result[b - 1] = result[b - 1], result[a - 1]

    return result

def main():
    # Read the input
    n, m = map(int, input().split())
    permutation = list(map(int, input().split()))
    allowed_swaps = []
    for _ in range(m):
        a, b = map(int, input().split())
        allowed_swaps.append((a, b))

    # Get the minimum number of swaps required to transform the permutation to 1, 2, ..., N
    swaps = get_permutation_swaps(permutation, allowed_swaps)

    # Get the permutation obtained by applying the swaps to the initial permutation
    result = get_permutation_from_swaps(permutation, allowed_swaps)

    # Print the result
    print(swaps)
    print(result)

if __name__ == '__main__':
    main()

