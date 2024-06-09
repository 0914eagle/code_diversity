
def solve(n, m, courses):
    # Initialize a list to store the maximum number of calories Stan can eat in each hour
    max_calories = [0] * n

    # Set the maximum number of calories Stan can eat in the first hour
    max_calories[0] = m

    # Loop through the remaining hours
    for i in range(1, n):
        # If the current hour has a non-zero number of calories
        if courses[i] != 0:
            # Set the maximum number of calories Stan can eat in the current hour
            max_calories[i] = max_calories[i-1] // 2
        # Otherwise, if the current hour has zero calories
        else:
            # Set the maximum number of calories Stan can eat in the current hour to zero
            max_calories[i] = 0

    # Return the sum of the maximum number of calories Stan can eat in each hour
    return sum(max_calories)

