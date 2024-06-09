
def get_cheerleading_tactic(n_cheerleaders, cheer_duration, spied_cheerleading_schedule):
    # Initialize variables
    sportify_goals = 0
    spoilify_goals = 0
    current_cheerleading_interval = 0
    current_cheerleading_duration = 0

    # Iterate through the spied cheerleading schedule
    for cheerleading_interval in spied_cheerleading_schedule:
        # Check if the current cheerleading interval overlaps with the current Sportify cheerleading interval
        if current_cheerleading_interval <= cheerleading_interval[0] <= current_cheerleading_interval + cheer_duration:
            # Calculate the overlap duration
            overlap_duration = min(current_cheerleading_interval + cheer_duration, cheerleading_interval[1]) - max(current_cheerleading_interval, cheerleading_interval[0])

            # Update the current Sportify cheerleading duration
            current_cheerleading_duration += overlap_duration

            # Check if the current Sportify cheerleading duration is greater than the 5 minute interval
            if current_cheerleading_duration >= 5:
                # Increment the Sportify goals
                sportify_goals += 1

                # Reset the current Sportify cheerleading duration
                current_cheerleading_duration = 0

        # Check if the current Sportify cheerleading interval overlaps with the current Spoilify cheerleading interval
        elif current_cheerleading_interval <= cheerleading_interval[1] <= current_cheerleading_interval + cheer_duration:
            # Calculate the overlap duration
            overlap_duration = min(current_cheerleading_interval + cheer_duration, cheerleading_interval[1]) - max(current_cheerleading_interval, cheerleading_interval[0])

            # Update the current Spoilify cheerleading duration
            current_cheerleading_duration += overlap_duration

            # Check if the current Spoilify cheerleading duration is greater than the 5 minute interval
            if current_cheerleading_duration >= 5:
                # Increment the Spoilify goals
                spoilify_goals += 1

                # Reset the current Spoilify cheerleading duration
                current_cheerleading_duration = 0

        # Check if the current Sportify cheerleading interval is before the current Spoilify cheerleading interval
        elif current_cheerleading_interval < cheerleading_interval[0]:
            # Increment the current Sportify cheerleading interval
            current_cheerleading_interval = cheerleading_interval[0]

            # Check if the current Sportify cheerleading interval is greater than the 5 minute interval
            if current_cheerleading_interval >= 5:
                # Increment the Sportify goals
                sportify_goals += 1

                # Reset the current Sportify cheerleading duration
                current_cheerleading_duration = 0

        # Check if the current Sportify cheerleading interval is after the current Spoilify cheerleading interval
        elif current_cheerleading_interval > cheerleading_interval[1]:
            # Increment the current Sportify cheerleading interval
            current_cheerleading_interval = cheerleading_interval[1]

            # Check if the current Sportify cheerleading interval is greater than the 5 minute interval
            if current_cheerleading_interval >= 5:
                # Increment the Sportify goals
                sportify_goals += 1

                # Reset the current Sportify cheerleading duration
                current_cheerleading_duration = 0

    # Return the results
    return sportify_goals, spoilify_goals

