
def get_sorted_permutation(permutation):
    n = len(permutation)
    # Initialize the array of swaps
    swaps = []
    # Loop through each pair of indices
    for i in range(n):
        for j in range(i+1, n):
            # If the difference between the indices is greater than or equal to n/2, add the swap to the list of swaps
            if abs(i - j) >= n//2:
                swaps.append([i, j])
    # Return the list of swaps
    return swaps

def perform_swaps(permutation, swaps):
    # Loop through each swap
    for swap in swaps:
        # Swap the elements at the given indices
        permutation[swap[0]], permutation[swap[1]] = permutation[swap[1]], permutation[swap[0]]
    # Return the sorted permutation
    return permutation

if __name__ == '__main__':
    n = int(input())
    permutation = list(map(int, input().split()))
    swaps = get_sorted_permutation(permutation)
    print(len(swaps))
    for swap in swaps:
        print(*swap)

