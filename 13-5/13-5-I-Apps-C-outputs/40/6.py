
def solve(n, firings, hirings):
    # Initialize the number of HR people as 1
    k = 1
    # Initialize the HR person in charge of the firing and hiring on day 1
    hr_person = 1
    # Loop through the remaining days
    for i in range(2, n+1):
        # If the number of firings on the current day is greater than the number of hirings, update the number of HR people
        if firings[i-1] > hirings[i-1]:
            k += 1
        # If the number of firings on the current day is equal to the number of hirings, do not update the number of HR people
        elif firings[i-1] == hirings[i-1]:
            pass
        # If the number of firings on the current day is less than the number of hirings, decrease the number of HR people
        else:
            k -= 1
        # Update the HR person in charge of the firing and hiring on the current day
        hr_person = (hr_person % k) + 1
    # Return the smallest number of HR people needed and the HR person in charge of the firing and hiring on each day
    return k, [hr_person for _ in range(n)]

