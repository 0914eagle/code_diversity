
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
        # If the current topic is different from the previous topic, start a new contest
        if topic != current_topic:
            current_topic = topic
            current_count = 1
        # Otherwise, increment the count
        else:
            current_count += 1

        # If the current count is greater than the maximum count, update the maximum count
        if current_count > max_count:
            max_count = current_count

        # If the current count is twice the previous count, start a new contest
        if current_count == 2 * contests[-1][1] if contests else 1:
            contests.append((current_topic, current_count))
            current_count = 1

    # Return the maximum count
    return max_count

