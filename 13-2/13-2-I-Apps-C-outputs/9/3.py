
def is_possible(n):
    # Initialize a list to store the positions of the swaps
    swaps = []

    # Iterate through all pairs of positions
    for i in range(n):
        for j in range(i + 1, n):
            # If the positions are not already swapped, swap them
            if i != j:
                swaps.append((i, j))

    # If the length of the swaps list is equal to the number of pairs of positions, return "YES" and the swaps
    if len(swaps) == n * (n - 1) // 2:
        return "YES\n" + "\n".join([f"{a} {b}" for a, b in swaps])
    else:
        return "NO"

if __name__ == '__main__':
    n = int(input())
    print(is_possible(n))

