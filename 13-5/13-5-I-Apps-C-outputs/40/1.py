
def solve(n, firings, hirings):
    # Initialize the number of HR people needed
    k = 1
    # Initialize the HR person in charge of the firing and hiring on day 1
    hr_person = 1
    # Loop through the remaining days
    for i in range(2, n+1):
        # If the number of firings on the current day is greater than the number of hirings, update the number of HR people needed
        if firings[i-1] > hirings[i-1]:
            k += 1
        # If the number of hirings on the current day is greater than the number of firings, update the HR person in charge
        elif hirings[i-1] > firings[i-1]:
            hr_person = (hr_person % k) + 1
    # Return the number of HR people needed and the HR person in charge for each day
    return k, [hr_person for _ in range(n)]

