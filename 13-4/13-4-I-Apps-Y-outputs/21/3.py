
def get_min_operations(heights):
    # Initialize variables
    n = len(heights)
    min_operations = 0
    max_height = max(heights)

    # Loop through each height and check if it can be achieved with the current operations
    for i in range(n):
        if heights[i] < max_height:
            # If the height cannot be achieved with the current operations, increase the minimum number of operations required
            min_operations += 1

    return min_operations

def main():
    # Read the input data
    n = int(input())
    heights = list(map(int, input().split()))

    # Call the function to get the minimum number of operations required
    min_operations = get_min_operations(heights)

    # Print the result
    print(min_operations)

if __name__ == '__main__':
    main()

