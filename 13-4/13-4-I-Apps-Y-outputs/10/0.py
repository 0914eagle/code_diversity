
def solve(n, combinations):
    # Initialize a dictionary to store the popularity of each combination
    popularity = {}

    # Iterate over the combinations and increment the popularity count for each combination
    for combination in combinations:
        combination_str = "".join(sorted(str(c) for c in combination))
        if combination_str in popularity:
            popularity[combination_str] += 1
        else:
            popularity[combination_str] = 1

    # Find the combination with the highest popularity
    most_popular_combination = max(popularity, key=popularity.get)

    # Return the number of frosh taking the most popular combination
    return popularity[most_popular_combination]

