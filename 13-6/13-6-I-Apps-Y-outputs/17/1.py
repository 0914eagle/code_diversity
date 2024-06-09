
def thematic_contests(n, a):
    # Sort the array of topics in increasing order
    a.sort()
    # Initialize the maximum number of problems to 0
    max_problems = 0
    # Initialize the current number of problems to 0
    current_problems = 0
    # Initialize the previous topic to -1 (no previous topic)
    previous_topic = -1
    # Iterate over the array of topics
    for topic in a:
        # If the current topic is different from the previous topic
        if topic != previous_topic:
            # Add the current number of problems to the maximum number of problems
            max_problems += current_problems
            # Reset the current number of problems to 0
            current_problems = 0
        # Increment the current number of problems
        current_problems += 1
        # Update the previous topic
        previous_topic = topic
    # Add the last set of problems to the maximum number of problems
    max_problems += current_problems
    # Return the maximum number of problems
    return max_problems

