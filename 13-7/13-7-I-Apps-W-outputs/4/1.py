
def get_allowed_values(k, values):
    # Sort the values in increasing order
    sorted_values = sorted(values)
    # Select the k values that minimize the sum of squared errors
    return sorted_values[:k]

def get_sum_of_squared_errors(allowed_values, values):
    # Calculate the sum of squared errors for the given allowed values
    sum_of_squared_errors = 0
    for value in values:
        # Find the closest allowed value to the current value
        closest_value = min(allowed_values, key=lambda x: abs(x - value))
        # Calculate the squared error for the current value
        squared_error = (value - closest_value) ** 2
        # Add the squared error to the total sum
        sum_of_squared_errors += squared_error
    return sum_of_squared_errors

def main():
    # Read the input
    d, k = map(int, input().split())
    values = []
    for _ in range(d):
        r, p = map(int, input().split())
        values.extend([r] * p)
    # Get the allowed values
    allowed_values = get_allowed_values(k, values)
    # Calculate the sum of squared errors
    sum_of_squared_errors = get_sum_of_squared_errors(allowed_values, values)
    # Print the result
    print(sum_of_squared_errors)

if __name__ == '__main__':
    main()

