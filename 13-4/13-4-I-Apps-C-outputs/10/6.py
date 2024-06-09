
def solve(n, m, courses):
    # Initialize a list to store the maximum number of calories that can be eaten in each hour
    max_calories = [0] * n

    # Initialize the maximum number of calories that can be eaten in the first hour
    max_calories[0] = m

    # Loop through the courses
    for i in range(1, n):
        # Calculate the maximum number of calories that can be eaten in the current hour
        max_calories[i] = max_calories[i - 1] // 2

        # If the current course has more calories than the maximum number of calories that can be eaten in the current hour, update the maximum number of calories that can be eaten in the current hour
        if courses[i] > max_calories[i]:
            max_calories[i] = courses[i]

    # Return the sum of the maximum number of calories that can be eaten in each hour
    return sum(max_calories)

