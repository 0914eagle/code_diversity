
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
    print(is_possible(n))

if __name__ == '__main__':
    main()

