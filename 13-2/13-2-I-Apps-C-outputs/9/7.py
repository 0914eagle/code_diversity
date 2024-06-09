
def is_possible(n):
    # Initialize a list to store the positions of the swaps
    swaps = []

    # Iterate through each pair of positions (i, j) where i < j
    for i in range(n):
        for j in range(i + 1, n):
            # If the swap (i, j) has not been performed yet
            if (i, j) not in swaps:
                # Perform the swap and add it to the list of swaps
                swaps.append((i, j))

    # If all pairs of positions have been swapped, return "YES" and the list of swaps
    if len(swaps) == n * (n - 1) // 2:
        return "YES", swaps
    else:
        return "NO", []

def main():
    n = int(input())
    result = is_possible(n)
    if result[0] == "YES":
        for swap in result[1]:
            print(swap[0], swap[1])
    else:
        print(result[0])

if __name__ == "__main__":
    main()

