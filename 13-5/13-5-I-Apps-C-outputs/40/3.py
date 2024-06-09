
def solve(n, firings, hirings):
    # Initialize the number of HR people needed
    k = 1
    # Initialize the HR person in charge of each day
    hiring_hr = [1] * n
    firing_hr = [1] * n
    # Loop through each day
    for i in range(1, n):
        # Calculate the number of workers fired and hired on this day
        fired = firings[i]
        hired = hirings[i]
        # If the number of workers fired is greater than the number of currently employed workers, adjust the number of HR people needed
        if fired > sum(hirings[:i]) - sum(firings[:i]):
            k += 1
        # Assign a different HR person to the firing and hiring on this day
        hiring_hr[i] = k
        firing_hr[i] = k - 1 if k > 1 else 1
    # Return the smallest number of HR people needed and the HR person in charge of each day
    return k, hiring_hr

