
def get_min_watering_operations(heights):
    # Initialize variables
    min_operations = 0
    current_heights = [0] * len(heights)

    # Loop through the heights and check if the current height is greater than the desired height
    for i, desired_height in enumerate(heights):
        if current_heights[i] < desired_height:
            # Increase the height of the current flower by 1
            current_heights[i] += 1
            min_operations += 1

    # Return the minimum number of watering operations required
    return min_operations

def main():
    # Read the number of flowers and their desired heights from stdin
    num_flowers = int(input())
    heights = list(map(int, input().split()))

    # Call the get_min_watering_operations function and print the result
    print(get_min_watering_operations(heights))

if __name__ == '__main__':
    main()

