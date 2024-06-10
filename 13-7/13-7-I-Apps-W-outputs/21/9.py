
def get_min_operations(heights):
    # Initialize variables
    operations = 0
    current_height = 0

    # Iterate through the heights and check if the current height is greater than or equal to the previous height
    for i in range(len(heights)):
        if heights[i] >= current_height:
            current_height = heights[i]
        else:
            operations += 1
            current_height = heights[i]

    return operations

def main():
    # Read the number of test cases
    num_test_cases = int(input())

    # Iterate through the test cases
    for _ in range(num_test_cases):
        # Read the number of supports and their heights
        num_supports = int(input())
        heights = list(map(int, input().split()))

        # Get the minimum number of operations required to make the supports able to support the waterslide
        operations = get_min_operations(heights)

        # Print the minimum number of operations
        print(operations)

if __name__ == '__main__':
    main()

