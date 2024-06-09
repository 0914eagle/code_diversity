
def is_possible_to_swap_all_pairs(n):
    # Initialize a list to store the positions of the swaps
    swaps = []

    # Iterate through all pairs of positions
    for i in range(n):
        for j in range(i + 1, n):
            # Check if the swap is already done
            if [i, j] in swaps or [j, i] in swaps:
                continue

            # Add the swap to the list of swaps
            swaps.append([i, j])

    # Check if all pairs of positions are swapped
    if len(swaps) == n * (n - 1) // 2:
        return True
    else:
        return False

def get_swaps(n):
    # Initialize a list to store the positions of the swaps
    swaps = []

    # Iterate through all pairs of positions
    for i in range(n):
        for j in range(i + 1, n):
            # Check if the swap is already done
            if [i, j] in swaps or [j, i] in swaps:
                continue

            # Add the swap to the list of swaps
            swaps.append([i, j])

    # Return the list of swaps
    return swaps

if __name__ == '__main__':
    n = int(input())
    if is_possible_to_swap_all_pairs(n):
        print("YES")
        for swap in get_swaps(n):
            print(swap[0], swap[1])
    else:
        print("NO")

