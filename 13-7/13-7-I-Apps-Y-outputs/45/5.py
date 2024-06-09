
def solve(n):
    # Initialize a dictionary to store the count of each combination of courses
    combination_count = {}

    # Iterate over the input data
    for i in range(n):
        # Read the next line of input
        line = input().strip()

        # Split the line into a list of course numbers
        courses = [int(x) for x in line.split()]

        # Sort the list of course numbers to ensure that the combination is unique
        courses.sort()

        # Check if the combination of courses is already in the dictionary
        if courses not in combination_count:
            # If not, add it to the dictionary with a count of 1
            combination_count[courses] = 1
        else:
            # If it is already in the dictionary, increment its count
            combination_count[courses] += 1

    # Find the combination with the highest count
    most_popular_combination = max(combination_count, key=combination_count.get)

    # Return the count of frosh who took the most popular combination
    return combination_count[most_popular_combination]

