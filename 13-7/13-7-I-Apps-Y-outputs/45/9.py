
def solve(n, course_combinations):
    # Initialize a dictionary to store the count of each course combination
    course_count = {}

    # Iterate over the course combinations for each frosh
    for combination in course_combinations:
        # Check if the course combination is already in the dictionary
        if combination not in course_count:
            # If not, add it to the dictionary with a count of 1
            course_count[combination] = 1
        else:
            # If it is already in the dictionary, increment the count
            course_count[combination] += 1

    # Find the combination with the highest count
    most_popular_combination = max(course_count, key=course_count.get)

    # Return the number of frosh taking the most popular combination
    return course_count[most_popular_combination]

