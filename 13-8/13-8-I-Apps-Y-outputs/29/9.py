
def get_maximum_sum(a, b, k):
    # Sort both arrays in non-decreasing order
    a.sort()
    b.sort()
    # Initialize the maximum sum and the number of moves made so far
    max_sum = 0
    moves_made = 0
    # Loop through both arrays and find the maximum sum
    for i in range(len(a)):
        for j in range(len(b)):
            # Check if the current move is within the allowed number of moves
            if moves_made < k:
                # Calculate the sum of the two arrays after the swap
                sum_after_swap = a[i] + b[j]
                # Check if the sum is greater than the current maximum sum
                if sum_after_swap > max_sum:
                    # Update the maximum sum and the number of moves made
                    max_sum = sum_after_swap
                    moves_made += 1
    # Return the maximum sum
    return max_sum

