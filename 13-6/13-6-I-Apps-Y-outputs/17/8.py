
def get_max_problems(n, a):
    # Sort the array of topics in descending order
    a.sort(reverse=True)
    # Initialize variables to keep track of the current number of problems and the maximum number of problems
    current_problems = 0
    max_problems = 0
    # Loop through the array of topics
    for i in range(n):
        # If the current number of problems is even, add the current topic to the list of topics for the current contest
        if current_problems % 2 == 0:
            current_topics.append(a[i])
        # If the current number of problems is odd, add the current topic to the list of topics for the next contest
        else:
            next_topics.append(a[i])
        # Increase the current number of problems by 1
        current_problems += 1
        # If the current number of problems is greater than the maximum number of problems, update the maximum number of problems
        if current_problems > max_problems:
            max_problems = current_problems
    # Return the maximum number of problems
    return max_problems

