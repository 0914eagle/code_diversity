
def solve(n, courses):
    # Initialize a dictionary to store the count of each combination
    combination_count = {}

    # Iterate over the list of courses for each frosh
    for course_list in courses:
        # Sort the list of courses for each frosh to ensure consistent ordering
        sorted_course_list = sorted(course_list)

        # Check if the combination of courses is already in the dictionary
        if tuple(sorted_course_list) in combination_count:
            # If it is, increment the count
            combination_count[tuple(sorted_course_list)] += 1
        else:
            # If it's not, add it to the dictionary with a count of 1
            combination_count[tuple(sorted_course_list)] = 1

    # Find the combination with the highest count
    most_popular_combination = max(combination_count, key=combination_count.get)

    # Return the count of frosh taking the most popular combination
    return combination_count[most_popular_combination]

