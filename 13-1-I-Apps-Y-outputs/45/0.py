
def solve(n, combinations):
    # Initialize a dictionary to store the popularity of each combination
    popularity = {}

    # Iterate over the combinations and increment the popularity of each combination
    for combination in combinations:
        if combination in popularity:
            popularity[combination] += 1
        else:
            popularity[combination] = 1

    # Find the combination with the highest popularity
    most_popular_combination = max(popularity, key=popularity.get)

    # Return the number of frosh taking the most popular combination
    return popularity[most_popular_combination]

