
def get_posterized_values(red_values, k):
    # Sort the red values in increasing order
    sorted_red_values = sorted(red_values)

    # Initialize the posterized values as the first k red values
    posterized_values = sorted_red_values[:k]

    # Initialize the sum of squared errors to 0
    sum_squared_errors = 0

    # Loop through each red value and calculate the sum of squared errors for that value
    for red_value in sorted_red_values:
        # Find the closest posterized value to the current red value
        closest_posterized_value = min(posterized_values, key=lambda x: abs(x - red_value))

        # Calculate the squared error for the current red value
        squared_error = (red_value - closest_posterized_value) ** 2

        # Add the squared error to the total sum of squared errors
        sum_squared_errors += squared_error

    return sum_squared_errors

def main():
    # Read the input from stdin
    d, k = map(int, input().split())
    red_values = []
    for _ in range(d):
        red_value, count = map(int, input().split())
        red_values.extend([red_value] * count)

    # Call the get_posterized_values function to get the sum of squared errors for the optimally chosen set of posterized values
    sum_squared_errors = get_posterized_values(red_values, k)

    # Print the sum of squared errors
    print(sum_squared_errors)

if __name__ == '__main__':
    main()

