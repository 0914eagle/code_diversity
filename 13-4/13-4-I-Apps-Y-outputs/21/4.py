
def get_min_watering_operations(heights):
    # Initialize variables
    min_operations = 0
    current_heights = [0] * len(heights)

    # Loop through the heights and check if they need to be increased
    for i, height in enumerate(heights):
        if height > current_heights[i]:
            current_heights[i] = height
            min_operations += 1

    # Return the minimum number of watering operations required
    return min_operations

def main():
    # Read the input data
    num_flowers, *heights = map(int, input().split())

    # Call the function to get the minimum number of watering operations
    min_operations = get_min_watering_operations(heights)

    # Print the result
    print(min_operations)

if __name__ == '__main__':
    main()

