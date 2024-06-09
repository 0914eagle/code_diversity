
def get_most_popular_combination(n, combinations):
    # Initialize a dictionary to store the count of each combination
    combination_count = {}

    # Iterate over the combinations and increment the count for each one
    for combination in combinations:
        if combination in combination_count:
            combination_count[combination] += 1
        else:
            combination_count[combination] = 1

    # Find the combination with the highest count
    most_popular_combination = max(combination_count, key=combination_count.get)

    # Return the count of the most popular combination
    return combination_count[most_popular_combination]

