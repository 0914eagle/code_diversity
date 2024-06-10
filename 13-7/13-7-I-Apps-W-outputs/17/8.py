
def get_possible_values(y, k, n):
    # Initialize an empty list to store the possible values of x
    possible_values = []
    
    # Iterate from 1 to n
    for x in range(1, n + 1):
        # Check if x + y is divisible by k
        if (x + y) % k == 0:
            # If it is, add it to the list of possible values
            possible_values.append(x)
    
    # Return the list of possible values
    return possible_values

def main():
    # Read the input
    y, k, n = map(int, input().split())
    
    # Get the list of possible values
    possible_values = get_possible_values(y, k, n)
    
    # Print the list of possible values
    print(*possible_values)

if __name__ == '__main__':
    main()

