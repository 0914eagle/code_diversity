
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
        # If the current topic is the same as the previous topic, increment the count
        if topic == current_topic:
            current_count += 1
        # If the current topic is different from the previous topic, reset the count
        else:
            current_topic = topic
            current_count = 1

        # If the current count is greater than the maximum count, update the maximum count
        if current_count > max_count:
            max_count = current_count

        # Add the problem to the result list
        result.append(i)

    # Return the result
    return result

