
def get_maximum_sum(matrix, k):
    # Initialize the maximum sum to 0
    max_sum = 0
    # Loop through each row of the matrix
    for row in matrix:
        # Initialize the sum of the current row to 0
        current_sum = 0
        # Loop through each element in the current row
        for element in row:
            # Check if the current element is divisible by k
            if element % k == 0:
                # Add the current element to the current sum
                current_sum += element
        # Check if the current sum is greater than the maximum sum
        if current_sum > max_sum:
            # Update the maximum sum
            max_sum = current_sum
    # Return the maximum sum
    return max_sum

