
def solve(n, courses):
    # Initialize a dictionary to store the popularity of each combination
    popularity = {}

    # Iterate over the input courses and increment the popularity of each combination
    for course_list in courses:
        course_set = set(course_list)
        if course_set in popularity:
            popularity[course_set] += 1
        else:
            popularity[course_set] = 1

    # Find the combination with the highest popularity
    max_popularity = max(popularity.values())

    # Return the number of frosh who chose the most popular combination
    return len([course_list for course_list, popularity in popularity.items() if popularity == max_popularity])

