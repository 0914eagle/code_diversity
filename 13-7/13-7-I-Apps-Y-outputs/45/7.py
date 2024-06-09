
def get_most_popular_combination(n, combinations):
    # Initialize a dictionary to store the popularity of each combination
    popularity = {}

    # Iterate over each combination and increment the popularity count for that combination
    for combination in combinations:
        if combination in popularity:
            popularity[combination] += 1
        else:
            popularity[combination] = 1

    # Find the combination with the highest popularity
    most_popular_combination = max(popularity, key=popularity.get)

    # Return the number of frosh taking the most popular combination
    return popularity[most_popular_combination]

