
def solve(n, courses):
    # Initialize a dictionary to store the count of each combination of courses
    combination_count = {}

    # Iterate over the list of courses for each frosh
    for course_list in courses:
        # Sort the list of courses for each frosh to ensure that the combinations are unique
        sorted_courses = sorted(course_list)

        # Check if the combination of courses is already in the dictionary
        if tuple(sorted_courses) in combination_count:
            # If it is, increment the count by 1
            combination_count[tuple(sorted_courses)] += 1
        else:
            # If it's not, add it to the dictionary with a count of 1
            combination_count[tuple(sorted_courses)] = 1

    # Find the combination with the highest count
    most_popular_combination = max(combination_count, key=combination_count.get)

    # Return the count of frosh taking the most popular combination
    return combination_count[most_popular_combination]

