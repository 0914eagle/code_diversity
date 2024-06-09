
def get_maximum_sum(matrix, k):
    # Initialize the maximum sum to 0
    max_sum = 0
    # Loop through each row of the matrix
    for row in matrix:
        # Get the number of elements that can be chosen in this row
        num_elements = int(len(row) / 2)
        # Initialize a sum variable for this row
        row_sum = 0
        # Loop through the first num_elements elements of the row
        for i in range(num_elements):
            # Add the element to the row sum
            row_sum += row[i]
        # If the row sum is divisible by k and is greater than the maximum sum, update the maximum sum
        if row_sum % k == 0 and row_sum > max_sum:
            max_sum = row_sum
    # Return the maximum sum
    return max_sum

