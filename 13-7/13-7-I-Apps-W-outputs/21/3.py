
def get_min_operations(heights):
    # Initialize variables
    n = len(heights)
    operations = 0
    max_height = 0

    # Iterate through the heights and check if the array is nondecreasing
    for i in range(n):
        if heights[i] <= max_height:
            max_height = heights[i]
        else:
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

        # Find the minimum number of operations needed to make the supports nondecreasing
        operations = get_min_operations(heights)

        # Print the result
        print(operations)

if __name__ == '__main__':
    main()

