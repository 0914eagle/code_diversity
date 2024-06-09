
def solve(n, combinations):
    # Initialize a dictionary to store the count of each combination
    combination_count = {}

    # Iterate over the combinations and increment the count of each combination
    for combination in combinations:
        if combination in combination_count:
            combination_count[combination] += 1
        else:
            combination_count[combination] = 1

    # Find the combination with the highest count
    most_popular_combination = max(combination_count, key=combination_count.get)

    # Return the number of frosh taking the most popular combination
    return combination_count[most_popular_combination]

