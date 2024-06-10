
def get_min_value(N, K):
    # Initialize the current value to 1
    curr_value = 1
    # Initialize the minimum value to 1
    min_value = 1
    # Loop through the number of operations
    for _ in range(N):
        # If the current value is even, double it
        if curr_value % 2 == 0:
            curr_value *= 2
        # If the current value is odd, add K to it
        else:
            curr_value += K
        # Update the minimum value if the current value is smaller than the minimum value
        min_value = min(min_value, curr_value)
    # Return the minimum value
    return min_value

def main():
    # Read the number of operations and the value of K from stdin
    N, K = map(int, input().split())
    # Call the get_min_value function and print the result
    print(get_min_value(N, K))

if __name__ == '__main__':
    main()

