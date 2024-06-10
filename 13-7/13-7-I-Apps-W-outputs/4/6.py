
def get_posterized_red_intensities(red_intensities, k):
    # Sort the red intensities in ascending order
    sorted_red_intensities = sorted(red_intensities)

    # Initialize the posterized red intensities with the first k values
    posterized_red_intensities = sorted_red_intensities[:k]

    # Initialize the sum of squared errors to 0
    sum_squared_errors = 0

    # Loop through each red intensity value
    for red_intensity in sorted_red_intensities:
        # Find the closest posterized red intensity to the current red intensity
        closest_posterized_red_intensity = min(posterized_red_intensities, key=lambda x: abs(x - red_intensity))

        # Calculate the squared error for the current red intensity
        squared_error = (red_intensity - closest_posterized_red_intensity) ** 2

        # Add the squared error to the total sum of squared errors
        sum_squared_errors += squared_error

    return sum_squared_errors

def get_optimal_posterized_red_intensities(red_intensities, k):
    # Initialize the optimal posterized red intensities as the first k red intensities
    optimal_posterized_red_intensities = red_intensities[:k]

    # Initialize the minimum sum of squared errors as the sum of squared errors for the first k red intensities
    minimum_sum_squared_errors = get_posterized_red_intensities(red_intensities, k)

    # Loop through each possible subset of red intensities
    for i in range(k, len(red_intensities) + 1):
        # Get the combination of red intensities
        combination = combinations(red_intensities, i)

        # Loop through each combination of red intensities
        for c in combination:
            # Get the sum of squared errors for the current combination of red intensities
            sum_squared_errors = get_posterized_red_intensities(c, k)

            # If the current combination of red intensities has a lower sum of squared errors than the previous minimum, update the optimal posterized red intensities and the minimum sum of squared errors
            if sum_squared_errors < minimum_sum_squared_errors:
                optimal_posterized_red_intensities = c
                minimum_sum_squared_errors = sum_squared_errors

    return optimal_posterized_red_intensities

def main():
    # Read the input red intensities and the number of allowed red intensities from stdin
    d, k = map(int, input().split())
    red_intensities = []
    for _ in range(d):
        red_intensity, _ = map(int, input().split())
        red_intensities.append(red_intensity)

    # Get the optimal posterized red intensities
    optimal_posterized_red_intensities = get_optimal_posterized_red_intensities(red_intensities, k)

    # Print the sum of squared errors for the optimal posterized red intensities
    print(get_posterized_red_intensities(optimal_posterized_red_intensities, k))

if __name__ == '__main__':
    main()

