
def solve(k2, k3, k5, k6):
    # Initialize the maximum sum to 0
    max_sum = 0
    # Loop through all possible combinations of digits
    for i in range(k2 + 1):
        for j in range(k3 + 1):
            for k in range(k5 + 1):
                for l in range(k6 + 1):
                    # Check if the current combination is valid
                    if i + j + k + l <= k2 and j <= k3 and k <= k5 and l <= k6:
                        # Calculate the sum of the current combination
                        sum = i * 2 + j * 3 + k * 5 + l * 6
                        # Update the maximum sum if necessary
                        max_sum = max(max_sum, sum)
    # Return the maximum sum
    return max_sum

