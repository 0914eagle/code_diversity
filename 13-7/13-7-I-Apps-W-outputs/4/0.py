
def find_optimized_values(k, red_values):
    # Sort the red values in increasing order
    red_values.sort()
    # Initialize the minimum sum of squared errors to a large value
    min_sum_squared_errors = float('inf')
    # Initialize the optimized values to be empty
    optimized_values = []
    # Iterate over all possible combinations of k allowed values
    for combination in itertools.combinations(red_values, k):
        # Calculate the sum of squared errors for this combination
        sum_squared_errors = 0
        for value in red_values:
            # Find the closest allowed value to the current value
            closest_value = min(combination, key=lambda x: abs(x - value))
            # Calculate the squared error for this value
            squared_error = (value - closest_value) ** 2
            # Add the squared error to the total sum
            sum_squared_errors += squared_error
        # If the sum of squared errors for this combination is less than the minimum, update the minimum and the optimized values
        if sum_squared_errors < min_sum_squared_errors:
            min_sum_squared_errors = sum_squared_errors
            optimized_values = list(combination)
    # Return the optimized values and the minimum sum of squared errors
    return optimized_values, min_sum_squared_errors

def main():
    # Read the input data
    d, k = map(int, input().split())
    red_values = []
    for _ in range(d):
        r, p = map(int, input().split())
        red_values.extend([r] * p)
    # Find the optimized values and the minimum sum of squared errors
    optimized_values, min_sum_squared_errors = find_optimized_values(k, red_values)
    # Print the minimum sum of squared errors
    print(min_sum_squared_errors)

if __name__ == '__main__':
    main()

