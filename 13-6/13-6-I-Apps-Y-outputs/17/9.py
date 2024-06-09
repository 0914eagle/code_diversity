
def thematic_contests(n, a):
    # Sort the problems by topic
    sorted_problems = sorted(enumerate(a), key=lambda x: x[1])

    # Initialize the variables
    current_topic = 0
    current_count = 0
    max_count = 0
    result = []

    # Iterate through the sorted problems
    for i, topic in sorted_problems:
        # If the current topic is the same as the previous topic, increase the count
        if topic == current_topic:
            current_count += 1
        # If the current topic is different from the previous topic, start a new contest
        else:
            # Add the current contest to the result
            result.append((current_topic, current_count))
            # Update the maximum count
            max_count = max(max_count, current_count)
            # Reset the current count and topic
            current_count = 1
            current_topic = topic

    # Add the last contest to the result
    result.append((current_topic, current_count))
    max_count = max(max_count, current_count)

    return max_count

