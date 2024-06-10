
def get_min_operations(heights):
    # Initialize variables
    operations = 0
    current_height = 0

    # Iterate through the heights
    for height in heights:
        # If the current height is less than or equal to the previous height, increase the operation count
        if height <= current_height:
            operations += 1
        # Update the current height
        current_height = height

    # Return the minimum number of operations
    return operations

def main():
    # Read the number of test cases
    num_test_cases = int(input())

    # Iterate through the test cases
    for _ in range(num_test_cases):
        # Read the number of supports
        num_supports = int(input())

        # Read the heights of the supports
        heights = list(map(int, input().split()))

        # Get the minimum number of operations
        min_operations = get_min_operations(heights)

        # Print the minimum number of operations
        print(min_operations)

if __name__ == '__main__':
    main()

