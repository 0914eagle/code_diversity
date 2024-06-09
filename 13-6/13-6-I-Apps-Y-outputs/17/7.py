
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
        # If the current topic is the same as the previous one, add the problem to the current contest
        if topic == current_topic:
            current_count += 1
        # If the current topic is different from the previous one, start a new contest
        else:
            result.append(current_count)
            current_topic = topic
            current_count = 1

    # Add the last contest
    result.append(current_count)

    # Return the maximum number of problems
    return max(result)

