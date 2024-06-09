
def thematic_contests(n, a):
    # Sort the problems by topic
    sorted_problems = sorted(enumerate(a), key=lambda x: x[1])

    # Initialize the variables
    current_topic = 0
    current_count = 0
    max_count = 0
    contests = []

    # Iterate through the sorted problems
    for i, topic in sorted_problems:
        # If the current topic is the same as the previous topic
        if topic == current_topic:
            # Increment the current count
            current_count += 1
        # If the current topic is different from the previous topic
        else:
            # Add the current topic and count to the contests list
            contests.append((current_topic, current_count))
            # Set the current topic and count to the new topic and count
            current_topic = topic
            current_count = 1

    # Add the last topic and count to the contests list
    contests.append((current_topic, current_count))

    # Iterate through the contests
    for i in range(len(contests) - 1):
        # Calculate the number of problems in the current contest
        current_count = contests[i + 1][1] - contests[i][1]
        # Check if the current count is greater than the max count
        if current_count > max_count:
            # Update the max count
            max_count = current_count

    # Return the max count
    return max_count

