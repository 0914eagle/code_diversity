
def solve(n, foreseeable_future):
    # Initialize variables
    hired = []
    fired = []
    hr_people = []
    hr_id = 1

    # Loop through the foreseeable future
    for day in range(n):
        # Get the number of workers fired and hired on this day
        f, h = foreseeable_future[day]

        # Fire the required number of workers
        for _ in range(f):
            fired.append(hired.pop())

        # Hire the required number of workers
        for _ in range(h):
            hired.append(hr_id)
            hr_id += 1

        # Assign an HR person to the firing and hiring on this day
        hr_people.append(hired.pop(0))

    # Return the smallest number of HR people needed and the HR person assignments
    return len(set(hr_people)), hr_people

