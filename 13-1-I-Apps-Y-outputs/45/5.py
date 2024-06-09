
def solve(n, courses):
    # Initialize a dictionary to store the count of each combination of courses
    course_count = {}

    # Iterate over the list of courses for each frosh
    for course_list in courses:
        # Sort the list of courses for each frosh to ensure that the same combination of courses is counted only once
        sorted_course_list = sorted(course_list)

        # Check if the combination of courses is already in the dictionary
        if sorted_course_list in course_count:
            # If it is, increment the count by 1
            course_count[sorted_course_list] += 1
        else:
            # If it's not, add it to the dictionary with a count of 1
            course_count[sorted_course_list] = 1

    # Find the combination of courses with the highest count
    most_popular_combination = max(course_count, key=course_count.get)

    # Return the count of frosh taking the most popular combination of courses
    return course_count[most_popular_combination]

