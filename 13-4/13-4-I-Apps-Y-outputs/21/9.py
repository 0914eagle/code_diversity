
def get_min_watering_operations(heights):
    # Initialize variables
    n = len(heights)
    min_operations = 0
    current_heights = [0] * n

    # Loop through each height and compare it to the current height
    for i in range(n):
        if heights[i] > current_heights[i]:
            # Increase the current height by 1 and increment the minimum number of operations
            current_heights[i] += 1
            min_operations += 1

    # Return the minimum number of operations required
    return min_operations

def main():
    # Read the number of flowers and their heights from stdin
    n = int(input())
    heights = list(map(int, input().split()))

    # Call the function to get the minimum number of watering operations
    min_operations = get_min_watering_operations(heights)

    # Print the result
    print(min_operations)

if __name__ == '__main__':
    main()

