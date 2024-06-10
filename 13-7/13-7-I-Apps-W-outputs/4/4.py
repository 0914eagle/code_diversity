
def get_posterized_values(red_values, k):
    # Sort the red values in increasing order
    sorted_red_values = sorted(red_values)

    # Initialize the allowed red values with the first k values
    allowed_red_values = sorted_red_values[:k]

    # Initialize the sum of squared errors to 0
    sum_squared_errors = 0

    # Loop through each red value and calculate the sum of squared errors for that value
    for red_value in sorted_red_values:
        # Find the closest allowed red value to the current red value
        closest_allowed_red_value = min(allowed_red_values, key=lambda x: abs(x - red_value))

        # Calculate the squared error for the current red value
        squared_error = (red_value - closest_allowed_red_value) ** 2

        # Add the squared error to the total sum of squared errors
        sum_squared_errors += squared_error

    return sum_squared_errors

def get_optimized_k(red_values, k_range):
    # Initialize the minimum sum of squared errors to a large value
    min_sum_squared_errors = float('inf')

    # Initialize the optimized k value to 0
    optimized_k = 0

    # Loop through each possible k value
    for k in k_range:
        # Get the sum of squared errors for the current k value
        sum_squared_errors = get_posterized_values(red_values, k)

        # If the current k value results in the smallest sum of squared errors, update the optimized k value
        if sum_squared_errors < min_sum_squared_errors:
            min_sum_squared_errors = sum_squared_errors
            optimized_k = k

    return optimized_k

def main():
    # Read the input data
    d, k = map(int, input().split())
    red_values = []
    for _ in range(d):
        red_value, _ = map(int, input().split())
        red_values.append(red_value)

    # Get the optimized k value
    optimized_k = get_optimized_k(red_values, range(1, k + 1))

    # Print the optimized k value
    print(optimized_k)

if __name__ == '__main__':
    main()

