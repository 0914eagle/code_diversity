
def solve(n, firings, hirings):
    # Initialize the number of HR people needed
    k = 1
    # Initialize the HR person in charge of the firing and hiring on each day
    hiring_hr = [1] * n
    firing_hr = [1] * n
    # Loop through each day
    for i in range(1, n):
        # Calculate the number of workers fired on the current day
        fired_today = firings[i]
        # Calculate the number of workers hired on the current day
        hired_today = hirings[i]
        # Calculate the total number of workers on the current day
        total_workers = firings[i-1] + hirings[i-1]
        # Check if the number of HR people needed has changed
        if fired_today > total_workers:
            # Increase the number of HR people needed
            k += 1
        # Assign the HR person in charge of the firing and hiring on the current day
        hiring_hr[i] = k
        firing_hr[i] = k - 1
    # Return the smallest number of HR people needed and the HR person in charge of the firing and hiring on each day
    return k, hiring_hr, firing_hr

