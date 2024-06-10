
def get_min_value(n, k):
    # Initialize the minimum value as 1
    min_value = 1
    # Iterate through the number of operations
    for _ in range(n):
        # Double the minimum value
        min_value *= 2
        # Increase the minimum value by K
        min_value += k
    # Return the minimum value
    return min_value

def main():
    # Read the number of operations and the value of K from stdin
    n, k = map(int, input().split())
    # Call the get_min_value function and print the result
    print(get_min_value(n, k))

if __name__ == '__main__':
    main()

