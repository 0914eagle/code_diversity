
def get_minimum_operations(s, t):
    # Initialize variables
    operations = 0
    i = 0

    # Loop through both strings simultaneously
    while i < len(s) and i < len(t):
        # If the characters at the current index are not the same, increment the operation count
        if s[i] != t[i]:
            operations += 1
        i += 1

    # Return the minimum number of operations required to convert s to t
    return operations

def main():
    # Read the input strings from stdin
    s = input()
    t = input()

    # Call the get_minimum_operations function and print the result
    print(get_minimum_operations(s, t))

if __name__ == '__main__':
    main()

