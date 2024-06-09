
def is_possible(n):
    # Initialize a list to store the positions of the swaps
    swaps = []

    # Iterate through all possible pairs of positions
    for i in range(n):
        for j in range(i + 1, n):
            # If the positions are not already swapped, swap them and add the positions to the list of swaps
            if i != j:
                swaps.append((i, j))

    # If the length of the list of swaps is equal to the number of pairs of positions, return "YES" and the list of swaps
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

