
def get_max_beauty(n, k, x, a):
    # Calculate the sum of beauty values of all pictures
    total_beauty = sum(a)

    # If x is greater than the number of pictures, return -1
    if x > n:
        return -1

    # Initialize variables for the maximum sum of beauty values and the current sum
    max_sum = 0
    current_sum = 0

    # Loop through the pictures and calculate the maximum sum of beauty values
    for i in range(n):
        # If the current sum is greater than the maximum sum, update the maximum sum
        if current_sum > max_sum:
            max_sum = current_sum

        # If the current sum is greater than or equal to the total beauty, break the loop
        if current_sum >= total_beauty:
            break

        # Add the beauty value of the current picture to the current sum
        current_sum += a[i]

        # If the current sum is greater than or equal to the total beauty, break the loop
        if current_sum >= total_beauty:
            break

        # If the current sum is greater than or equal to the maximum sum, break the loop
        if current_sum >= max_sum:
            break

    # Return the maximum sum of beauty values
    return max_sum

