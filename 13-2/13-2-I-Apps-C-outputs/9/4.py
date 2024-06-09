
def is_possible(n):
    # Initialize a list to store the positions of the swaps
    swaps = []

    # Iterate through each pair of positions
    for i in range(n):
        for j in range(i + 1, n):
            # If the positions are not already swapped
            if i != j:
                # Swap the positions and add them to the list of swaps
                swaps.append((i, j))

    # If all pairs of positions are swapped, return YES and the list of swaps
    if len(swaps) == n * (n - 1) // 2:
        return "YES\n" + "\n".join(str(swap) for swap in swaps)
    else:
        return "NO"

if __name__ == '__main__':
    n = int(input())
    print(is_possible(n))

