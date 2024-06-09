
def solve(cows_per_day, num_days):
    # Initialize a dictionary to store the number of farms that need inspection
    # for each day
    farms_needed = {}

    # Loop through each day
    for day in range(1, num_days + 1):
        # Initialize the number of farms that need inspection for this day
        farms_needed[day] = 0

        # Loop through each cow on each farm
        for i in range(len(cows_per_day)):
            # If the cow is on a farm with more than C cows, move half of them to a new farm
            if cows_per_day[i] > C:
                cows_per_day[i] = int(cows_per_day[i] / 2)
                farms_needed[day] += 1

        # Add the number of farms that need inspection for this day to the total
        farms_needed[day] += len([farm for farm in cows_per_day if farm > 0])

    # Return the number of farms that need inspection for each day
    return [farms_needed[day] for day in range(1, num_days + 1)]

