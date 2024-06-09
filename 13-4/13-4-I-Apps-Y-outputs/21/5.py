
def get_min_watering_operations(heights):
    # Initialize variables
    min_operations = 0
    current_heights = [0] * len(heights)

    # Loop through the heights and check if the current height is less than the desired height
    for i, desired_height in enumerate(heights):
        if current_heights[i] < desired_height:
            # Increase the current height by 1 and increment the number of operations
            current_heights[i] += 1
            min_operations += 1

    # Return the minimum number of operations required
    return min_operations

def main():
    # Read the number of flowers and their desired heights from stdin
    n = int(input())
    heights = list(map(int, input().split()))

    # Call the function to get the minimum number of watering operations required
    min_operations = get_min_watering_operations(heights)

    # Print the result
    print(min_operations)

if __name__ == '__main__':
    main()

