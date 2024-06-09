
def solve(n, firings, hirings):
    # Initialize the number of HR people needed
    k = 1
    # Initialize the HR person in charge of the firing and hiring on day 1
    hr_person = 1
    # Loop through the remaining days
    for i in range(2, n+1):
        # Calculate the number of workers fired on day i
        firing = firings[i-1]
        # Calculate the number of workers hired on day i
        hiring = hirings[i-1]
        # If the number of workers fired is greater than the number of workers hired,
        if firing > hiring:
            # Increment the number of HR people needed
            k += 1
            # Assign a new HR person to the firing and hiring on day i
            hr_person = k
        # Otherwise, if the number of workers fired is less than or equal to the number of workers hired,
        else:
            # Assign the same HR person to the firing and hiring on day i
            hr_person = (hr_person % k) + 1
    # Return the number of HR people needed and the HR person in charge of the firing and hiring on each day
    return k, [hr_person for _ in range(n)]

