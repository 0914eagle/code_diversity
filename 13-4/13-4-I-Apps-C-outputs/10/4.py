
def solve(n, m, courses):
    # Initialize a list to store the maximum number of calories Stan can eat in each hour
    max_calories = [0] * n

    # Initialize the maximum number of calories Stan can eat in the first hour
    max_calories[0] = m

    # Loop through the courses
    for i in range(1, n):
        # If the current course has more calories than the previous hour, update the maximum number of calories Stan can eat in the current hour
        if courses[i] > max_calories[i-1]:
            max_calories[i] = courses[i]
        # Otherwise, update the maximum number of calories Stan can eat in the current hour by dividing the previous hour's maximum number of calories by 2
        else:
            max_calories[i] = max_calories[i-1] // 2

    # Return the sum of the maximum number of calories Stan can eat in each hour
    return sum(max_calories)

