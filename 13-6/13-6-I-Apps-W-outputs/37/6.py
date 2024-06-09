
def get_potential_friends(x, y, k):
    # Convert x and y to binary
    x_bin = bin(x)[2:]
    y_bin = bin(y)[2:]
    # Initialize count of different bits
    diff_bits = 0
    # Loop through bits of x and y
    for i in range(len(x_bin)):
        if x_bin[i] != y_bin[i]:
            diff_bits += 1
    # Return number of potential friends
    if diff_bits <= k:
        return 1
    else:
        return 0

def main():
    # Read input
    n, m, k = map(int, input().split())
    x = [int(input()) for _ in range(m + 1)]
    # Initialize count of potential friends
    count = 0
    # Loop through players
    for i in range(m + 1):
        # Loop through players again
        for j in range(m + 1):
            # If players are not the same
            if i != j:
                # Get potential friends
                count += get_potential_friends(x[i], x[j], k)
    # Print count of potential friends
    print(count)

if __name__ == '__main__':
    main()

