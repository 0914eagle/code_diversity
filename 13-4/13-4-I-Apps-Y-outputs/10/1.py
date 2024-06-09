
def solve(n, courses):
    # Initialize a dictionary to store the popularity of each combination
    popularity = {}

    # Iterate over the input courses and update the popularity of each combination
    for course in courses:
        combination = tuple(course)
        if combination not in popularity:
            popularity[combination] = 0
        popularity[combination] += 1

    # Find the combination with the highest popularity
    most_popular = max(popularity, key=popularity.get)

    # Return the number of frosh taking the most popular combination
    return popularity[most_popular]

