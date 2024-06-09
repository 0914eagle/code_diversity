
def get_max_sum(k2, k3, k5, k6):
    # Initialize the maximum sum and the current sum
    max_sum = 0
    current_sum = 0
    
    # Loop through the digits and add them to the current sum
    for i in range(k2):
        current_sum += 2
    for i in range(k3):
        current_sum += 3
    for i in range(k5):
        current_sum += 5
    for i in range(k6):
        current_sum += 6
    
    # Check if the current sum is greater than the maximum sum
    if current_sum > max_sum:
        max_sum = current_sum
    
    # Return the maximum sum
    return max_sum

