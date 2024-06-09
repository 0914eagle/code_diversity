
def get_min_changes(s, t):
    # Initialize variables
    n = len(s)
    m = len(t)
    changes = 0
    positions = []

    # Iterate through the string s
    for i in range(n):
        # If the symbol at position i in s is not equal to the symbol at position i in t
        if s[i] != t[i]:
            # Increment the number of changes
            changes += 1
            # Add the position i to the list of positions
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

    # Print the output
    print(changes)
    print(*positions)

if __name__ == '__main__':
    main()

