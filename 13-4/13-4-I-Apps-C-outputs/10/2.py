
def solve(n, m, courses):
    # Initialize a list to store the maximum number of calories Stan can eat in each hour
    max_calories = [0] * n

    # Set the maximum number of calories for the first hour
    max_calories[0] = m

    # Loop through the remaining hours
    for i in range(1, n):
        # If the current hour has a non-zero number of calories, Stan can eat at the same rate as the previous hour
        if courses[i] != 0:
            max_calories[i] = max_calories[i-1]
        # Otherwise, Stan can eat at the same rate as the previous two hours
        else:
            max_calories[i] = max(max_calories[i-1], max_calories[i-2])

    # Return the sum of the maximum number of calories Stan can eat in each hour
    return sum(max_calories)

