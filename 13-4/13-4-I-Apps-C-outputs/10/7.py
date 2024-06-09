
def solve(n, m, courses):
    # Initialize a list to store the maximum number of calories Stan can eat in each hour
    max_calories = [0] * n

    # Initialize the maximum number of calories Stan can eat in the first hour
    max_calories[0] = m

    # Loop through the remaining hours
    for i in range(1, n):
        # If the current hour's course has more calories than the previous hour's course,
        # then Stan can eat the same amount as the previous hour
        if courses[i] > courses[i-1]:
            max_calories[i] = max_calories[i-1]
        # Otherwise, Stan can eat half the amount of the previous hour's course
        else:
            max_calories[i] = max_calories[i-1] // 2

    # Return the sum of the maximum number of calories Stan can eat in each hour
    return sum(max_calories)

