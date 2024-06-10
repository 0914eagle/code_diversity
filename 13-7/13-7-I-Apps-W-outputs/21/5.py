
def get_min_operations(heights):
    # Initialize variables
    n = len(heights)
    operations = 0
    i = 0

    # Iterate through the heights array
    while i < n:
        # Check if the current subarray is nondecreasing
        if all(heights[i+j] >= heights[i+j+1] for j in range(n-i-1)):
            # If it is, move to the next subarray
            i += 1
        else:
            # If it's not, perform an operation on the current subarray
            operations += 1
            for j in range(i, n):
                heights[j] += 1
            i = 0

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

