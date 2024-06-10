
def get_possible_x(y, k, n):
    # Initialize an empty list to store the possible values of x
    possible_x = []
    
    # Loop through all possible values of x
    for x in range(1, n + 1):
        # Check if x + y is divisible by k
        if (x + y) % k == 0:
            # If it is, add it to the list of possible values of x
            possible_x.append(x)
    
    # Return the list of possible values of x
    return possible_x

def main():
    # Read the input data
    y, k, n = map(int, input().split())
    
    # Call the get_possible_x function and store the result
    possible_x = get_possible_x(y, k, n)
    
    # Print the list of possible values of x
    print(*possible_x, sep=' ')

if __name__ == '__main__':
    main()

