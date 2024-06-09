
def get_min_changes(s, t):
    # Initialize variables
    n = len(s)
    m = len(t)
    changes = 0
    positions = []

    # Loop through each position in s
    for i in range(n):
        # If the symbol at the current position is not equal to the symbol at the corresponding position in t
        if s[i] != t[i]:
            # Increment the number of changes
            changes += 1
            # Add the current position to the list of positions
            positions.append(i+1)

    # Return the number of changes and the list of positions
    return changes, positions

def main():
    # Read the input
    n, m = map(int, input().split())
    s = input()
    t = input()

    # Call the function to get the minimum number of changes and the list of positions
    changes, positions = get_min_changes(s, t)

    # Print the number of changes
    print(changes)

    # Print the list of positions
    for position in positions:
        print(position)

if __name__ == '__main__':
    main()

