
def get_min_value(N, K):
    # Initialize the minimum value as 1
    min_value = 1
    # Loop through each operation
    for _ in range(N):
        # Operation A: double the current value
        min_value *= 2
        # Operation B: add K to the current value
        min_value += K
    # Return the minimum value
    return min_value

def main():
    # Read the input from stdin
    N, K = map(int, input().split())
    # Call the get_min_value function and print the result
    print(get_min_value(N, K))

if __name__ == '__main__':
    main()

