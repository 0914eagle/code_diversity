
def get_posterized_image(red_values, k):
    # Initialize a list to store the allowed red values
    allowed_red_values = []

    # Iterate through the red values and add the k most frequent values to the allowed red values list
    for i in range(k):
        allowed_red_values.append(red_values[i])

    # Initialize a variable to store the sum of squared errors
    sum_squared_errors = 0

    # Iterate through the original red values and calculate the sum of squared errors for each pixel
    for red_value in red_values:
        # Find the closest allowed red value to the current red value
        closest_allowed_red_value = min(allowed_red_values, key=lambda x: abs(x - red_value))

        # Calculate the squared error for the current pixel
        squared_error = (red_value - closest_allowed_red_value) ** 2

        # Add the squared error to the sum of squared errors
        sum_squared_errors += squared_error

    # Return the sum of squared errors
    return sum_squared_errors

def main():
    # Read the input data
    d, k = map(int, input().split())
    red_values = []
    for _ in range(d):
        red_value, pixel_count = map(int, input().split())
        red_values.append(red_value)

    # Sort the red values in increasing order
    red_values.sort()

    # Calculate the sum of squared errors for the optimally chosen set of k allowed integer values
    sum_squared_errors = get_posterized_image(red_values, k)

    # Print the sum of squared errors
    print(sum_squared_errors)

if __name__ == '__main__':
    main()

