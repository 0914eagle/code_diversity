
def thematic_contests(n, topics):
    # Sort the topics in decreasing order
    sorted_topics = sorted(topics, reverse=True)
    # Initialize the maximum number of problems to 0
    max_problems = 0
    # Initialize the current number of problems to 0
    current_problems = 0
    # Iterate through the sorted topics
    for topic in sorted_topics:
        # If the current number of problems is 0, set it to the number of problems with the current topic
        if current_problems == 0:
            current_problems = topics.count(topic)
        # Otherwise, double the current number of problems
        else:
            current_problems *= 2
        # Update the maximum number of problems if necessary
        max_problems = max(max_problems, current_problems)
    # Return the maximum number of problems
    return max_problems

