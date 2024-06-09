
def popular_combination(n):
    # Initialize a dictionary to store the count of each combination
    combination_count = {}

    # Iterate through the input list
    for i in range(n):
        # Get the current combination of courses
        combination = input().split()

        # Check if the combination is already in the dictionary
        if combination not in combination_count:
            # If not, add it to the dictionary with a count of 1
            combination_count[combination] = 1
        else:
            # If it is already in the dictionary, increment the count
            combination_count[combination] += 1

    # Find the combination with the highest count
    most_popular_combination = max(combination_count, key=combination_count.get)

    # Return the number of frosh taking the most popular combination
    return combination_count[most_popular_combination]

