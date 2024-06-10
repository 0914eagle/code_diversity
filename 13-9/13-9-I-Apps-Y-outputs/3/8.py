
def find_min_value(N, K):
    # Initialize the minimum value as 1
    min_value = 1
    # Loop through each operation
    for i in range(N):
        # If the current minimum value is even, double it
        if min_value % 2 == 0:
            min_value *= 2
        # Otherwise, add K to the minimum value
        else:
            min_value += K
    # Return the minimum value after all operations
    return min_value

def main():
    # Read the input from stdin
    N, K = map(int, input().split())
    # Use the find_min_value function to find the minimum value
    min_value = find_min_value(N, K)
    # Print the minimum value
    print(min_value)

if __name__ == '__main__':
    main()

