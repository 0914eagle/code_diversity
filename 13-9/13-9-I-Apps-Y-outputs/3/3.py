
def get_min_value(n, k):
    # Initialize the minimum value to be the starting value
    min_value = 1
    # Loop through the number of operations
    for _ in range(n):
        # Double the value
        min_value *= 2
        # Increase the value by K
        min_value += k
    # Return the minimum value
    return min_value

def main():
    # Read the number of operations and the increment value from stdin
    n, k = map(int, input().split())
    # Call the get_min_value function and print the result
    print(get_min_value(n, k))

if __name__ == '__main__':
    main()

