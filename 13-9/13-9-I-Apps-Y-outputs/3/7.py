
def get_min_value(N, K):
    # Initialize the minimum value as 1
    min_value = 1
    # Loop through each operation
    for i in range(N):
        # If the current minimum value is even, double it
        if min_value % 2 == 0:
            min_value *= 2
        # Otherwise, increase it by K
        else:
            min_value += K
    # Return the minimum value after all operations
    return min_value

def main():
    # Read the input from stdin
    N, K = map(int, input().split())
    # Get the minimum value after N operations
    min_value = get_min_value(N, K)
    # Print the minimum value
    print(min_value)

if __name__ == '__main__':
    main()

