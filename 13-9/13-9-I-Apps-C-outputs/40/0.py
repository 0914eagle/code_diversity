
def optimal_earnings(N, a):
    # Initialize a list to store the earnings for each gem
    earnings = [0] * (N + 1)
    # Loop through each gem and calculate the earnings
    for i in range(1, N + 1):
        # If the gem is not smashed, calculate the earnings
        if i % 2 == 1:
            earnings[i] = a[i - 1]
        # If the gem is smashed, calculate the earnings by adding the earnings of the previous gem
        else:
            earnings[i] = earnings[i - 1] + a[i - 1]
    # Return the maximum earnings
    return max(earnings)

