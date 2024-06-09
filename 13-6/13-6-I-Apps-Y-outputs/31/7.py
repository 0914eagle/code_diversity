
def get_min_operations(s, t):
    # Initialize variables
    operations = 0
    i, j = 0, 0

    # Loop through both strings simultaneously
    while i < len(s) and j < len(t):
        # If the characters are not the same, increment the operation count
        if s[i] != t[j]:
            operations += 1
        # Increment both indices
        i += 1
        j += 1

    # Return the minimum number of operations required
    return operations

def main():
    # Read the input strings from stdin
    s = input()
    t = input()

    # Call the get_min_operations function and print the result
    print(get_min_operations(s, t))

if __name__ == '__main__':
    main()

