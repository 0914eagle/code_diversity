
def get_most_popular_combination(num_frosh, course_combinations):
    # Initialize a dictionary to store the count of each combination
    combination_count = {}

    # Iterate over the course combinations for each frosh
    for courses in course_combinations:
        # Sort the courses to ensure that the combination is in a consistent format
        sorted_courses = sorted(courses)

        # Check if the combination is already in the dictionary
        if sorted_courses in combination_count:
            # If it is, increment the count
            combination_count[sorted_courses] += 1
        else:
            # If it's not, add it to the dictionary with a count of 1
            combination_count[sorted_courses] = 1

    # Find the combination with the highest count
    most_popular_combination = max(combination_count, key=combination_count.get)

    # Return the number of frosh taking the most popular combination
    return combination_count[most_popular_combination]

