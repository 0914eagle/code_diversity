
def solve(n, firings, hirings):
    # Initialize the number of HR people needed
    k = 1
    # Initialize the HR person in charge of the firing and hiring on each day
    hiring_hr = [1] * n
    # Loop through each day
    for i in range(1, n):
        # If the number of firings on the current day is greater than the number of hirings, increase the number of HR people needed
        if firings[i] > hirings[i]:
            k += 1
        # If the number of firings on the current day is equal to the number of hirings, assign the same HR person to both the firing and hiring
        elif firings[i] == hirings[i]:
            hiring_hr[i] = hiring_hr[i-1]
        # If the number of firings on the current day is less than the number of hirings, decrease the number of HR people needed
        else:
            k -= 1
    return k, hiring_hr

