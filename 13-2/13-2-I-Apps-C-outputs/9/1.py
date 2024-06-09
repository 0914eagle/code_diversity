
def is_possible(n):
    # Initialize a list to store the positions of the swaps
    swaps = []

    # Iterate through each pair of positions (i, j) where i < j
    for i in range(n):
        for j in range(i + 1, n):
            # If the swap (i, j) is not already in the list, add it
            if (i, j) not in swaps:
                swaps.append((i, j))

    # If the length of the swaps list is equal to the number of pairs of positions, return "YES"
    if len(swaps) == n * (n - 1) // 2:
        return "YES"
    else:
        return "NO"

def get_swaps(n):
    # Initialize a list to store the positions of the swaps
    swaps = []

    # Iterate through each pair of positions (i, j) where i < j
    for i in range(n):
        for j in range(i + 1, n):
            # If the swap (i, j) is not already in the list, add it
            if (i, j) not in swaps:
                swaps.append((i, j))

    # Return the list of swaps
    return swaps

if __name__ == '__main__':
    n = int(input())
    print(is_possible(n))
    if is_possible(n) == "YES":
        swaps = get_swaps(n)
        for swap in swaps:
            print(swap[0], swap[1])

