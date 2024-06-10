
def get_min_sum_of_squared_errors(k, d, red_values):
    # Initialize the minimum sum of squared errors to a large value
    min_sum = float('inf')
    # Initialize the optimal set of k allowed integer values
    optimal_values = []
    
    # Iterate over all possible sets of k allowed integer values
    for values in itertools.combinations(range(256), k):
        # Initialize the sum of squared errors for this set of values
        sum_of_squared_errors = 0
        # Iterate over all pixels in the image
        for red in red_values:
            # Find the closest allowed value to the current pixel's red intensity
            closest_value = min(values, key=lambda x: abs(x - red))
            # Calculate the squared error for this pixel
            squared_error = (red - closest_value) ** 2
            # Add the squared error to the total sum of squared errors
            sum_of_squared_errors += squared_error
        
        # If the sum of squared errors for this set of values is smaller than the minimum sum,
        # update the minimum sum and the optimal set of values
        if sum_of_squared_errors < min_sum:
            min_sum = sum_of_squared_errors
            optimal_values = list(values)
    
    return min_sum

def main():
    # Read the input from stdin
    d, k = map(int, input().split())
    red_values = []
    for _ in range(d):
        red, count = map(int, input().split())
        red_values += [red] * count
    
    # Call the get_min_sum_of_squared_errors function and print the result
    print(get_min_sum_of_squared_errors(k, d, red_values))

if __name__ == '__main__':
    main()

