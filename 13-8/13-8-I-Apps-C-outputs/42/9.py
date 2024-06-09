
def solve(n, t, m, spy_schedule):
    # Initialize the variables to keep track of the cheerleading schedule
    sportify_schedule = []
    spoilify_schedule = []
    current_time = 0

    # Loop through the spy schedule and add the intervals to the spoilify schedule
    for interval in spy_schedule:
        spoilify_schedule.append([interval[0], interval[1]])

    # Loop through the time intervals
    while current_time < 90:
        # Check if any cheerleaders from Sportify are cheering
        for i in range(n):
            # Check if the current time is within the interval for this cheerleader
            if current_time >= t * i and current_time < t * (i + 1):
                # Add the current time to the sportify schedule
                sportify_schedule.append(current_time)
                break

        # Check if any cheerleaders from Spoilify are cheering
        for interval in spoilify_schedule:
            # Check if the current time is within the interval for this cheerleader
            if current_time >= interval[0] and current_time < interval[1]:
                # Add the current time to the spoilify schedule
                spoilify_schedule.append(current_time)
                break

        # Increment the current time by 1 minute
        current_time += 1

    # Initialize the variables to keep track of the goals
    sportify_goals = 0
    spoilify_goals = 0

    # Loop through the schedule and check for 5 minute intervals with more cheers from Sportify
    for i in range(len(sportify_schedule) - 4):
        # Check if the next 5 minutes have more cheers from Sportify
        if sportify_schedule[i] in sportify_schedule[i:i+5]:
            sportify_goals += 1

    # Loop through the schedule and check for 5 minute intervals with more cheers from Spoilify
    for i in range(len(spoilify_schedule) - 4):
        # Check if the next 5 minutes have more cheers from Spoilify
        if spoilify_schedule[i] in spoilify_schedule[i:i+5]:
            spoilify_goals += 1

    # Return the results
    return [sportify_goals, spoilify_goals]

