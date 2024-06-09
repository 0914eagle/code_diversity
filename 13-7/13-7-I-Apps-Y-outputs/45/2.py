
def popular_combinations(num_frosh, combinations):
    # Initialize a dictionary to store the popularity of each combination
    popularity = {}

    # Iterate over each frosh and their selected courses
    for frosh in combinations:
        # Check if the combination of courses is already in the dictionary
        if frosh in popularity:
            # If it is, increment the popularity count
            popularity[frosh] += 1
        else:
            # If it's not, add it to the dictionary with a popularity count of 1
            popularity[frosh] = 1

    # Find the combination with the highest popularity
    most_popular = max(popularity, key=popularity.get)

    # Return the number of frosh taking the most popular combination
    return popularity[most_popular]

