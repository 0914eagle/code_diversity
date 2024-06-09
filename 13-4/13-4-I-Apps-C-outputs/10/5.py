
def solve(n, m, courses):
    # Initialize a list to store the maximum number of calories that can be eaten in each hour
    max_calories = [0] * n

    # Initialize the maximum number of calories that can be eaten in the first hour
    max_calories[0] = m

    # Loop through the courses and calculate the maximum number of calories that can be eaten in each hour
    for i in range(1, n):
        max_calories[i] = int(max_calories[i-1] / 2)

    # Loop through the courses and calculate the maximum number of calories that can be eaten in each hour
    for i in range(n):
        max_calories[i] = min(max_calories[i], courses[i])

    # Return the sum of the maximum number of calories that can be eaten in each hour
    return sum(max_calories)

