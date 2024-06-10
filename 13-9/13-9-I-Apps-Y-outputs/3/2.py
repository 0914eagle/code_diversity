
def get_min_value(N, K):
    # Initialize the minimum value as 1
    min_value = 1
    # Loop through the number of operations
    for _ in range(N):
        # Double the minimum value
        min_value *= 2
        # Increment the minimum value by K
        min_value += K
    # Return the minimum value
    return min_value

def main():
    # Read the number of operations and the increment value from stdin
    N, K = map(int, input().split())
    # Get the minimum value displayed in the board after N operations
    min_value = get_min_value(N, K)
    # Print the minimum value
    print(min_value)

if __name__ == '__main__':
    main()

