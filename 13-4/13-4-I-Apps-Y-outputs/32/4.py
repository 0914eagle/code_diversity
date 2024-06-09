
def get_min_value(N, K):
    # Initialize the minimum value as 1
    min_value = 1
    # Loop through the number of operations
    for _ in range(N):
        # Double the minimum value
        min_value *= 2
        # Add K to the minimum value
        min_value += K
    # Return the minimum value
    return min_value

if __name__ == '__main__':
    N, K = map(int, input().split())
    print(get_min_value(N, K))

