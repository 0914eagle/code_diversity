
def get_min_operations(heights):
    # Initialize variables
    n = len(heights)
    operations = 0
    max_height = 0

    # Iterate through the heights array
    for i in range(n):
        # If the current height is less than the maximum height, we need to perform an operation
        if heights[i] < max_height:
            operations += 1
            max_height = heights[i]
        else:
            max_height = max(max_height, heights[i])

    return operations

def main():
    # Read the number of test cases
    num_test_cases = int(input())

    # Iterate through the test cases
    for _ in range(num_test_cases):
        # Read the number of supports and their heights
        n = int(input())
        heights = list(map(int, input().split()))

        # Call the get_min_operations function and print the result
        print(get_min_operations(heights))

if __name__ == '__main__':
    main()

