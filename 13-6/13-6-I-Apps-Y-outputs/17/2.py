
def get_max_problems(n, a):
    # Sort the topics in ascending order
    sorted_topics = sorted(set(a))

    # Initialize the maximum number of problems to 0
    max_problems = 0

    # Loop through each topic
    for topic in sorted_topics:
        # Get the number of problems with the current topic
        num_problems = a.count(topic)

        # If the number of problems is greater than the maximum number of problems, update the maximum number of problems
        if num_problems > max_problems:
            max_problems = num_problems

    return max_problems

