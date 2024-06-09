
def get_min_hr_people(n, firings, hirings):
    # Initialize variables
    hr_people = 0
    current_firings = 0
    current_hirings = 0
    hr_id = 1
    hr_assignments = []

    # Loop through each day
    for i in range(n):
        # Calculate the number of firings and hirings on this day
        day_firings = firings[i] - current_firings
        day_hirings = hirings[i] - current_hirings

        # Update the current number of firings and hirings
        current_firings += day_firings
        current_hirings += day_hirings

        # If there are more firings than hirings, assign an HR person to fire employees
        if day_firings > day_hirings:
            hr_people += 1
            hr_assignments.append(hr_id)
            hr_id += 1

    # Return the minimum number of HR people needed and their assignments
    return hr_people, hr_assignments

