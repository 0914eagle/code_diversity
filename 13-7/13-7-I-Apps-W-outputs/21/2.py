
def get_min_operations(heights):
    # Initialize variables
    n = len(heights)
    operations = 0
    max_height = 0

    # Iterate through the heights and check if they are non-decreasing
    for i in range(n):
        if heights[i] > max_height:
            max_height = heights[i]
        elif heights[i] < max_height:
            operations += 1
            max_height = heights[i]

    return operations

def main():
    # Read the number of test cases
    num_test_cases = int(input())

    # Iterate through the test cases
    for _ in range(num_test_cases):
        # Read the number of supports and their heights
        n = int(input())
        heights = list(map(int, input().split()))

        # Get the minimum number of operations required to make the supports non-decreasing
        operations = get_min_operations(heights)

        # Print the result
        print(operations)

if __name__ == '__main__':
    main()

