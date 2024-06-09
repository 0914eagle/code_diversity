
def solve(problems, drinks):
    # Initialize a dictionary to store the time it takes to solve each problem
    problem_time = {}
    for problem, time in problems.items():
        problem_time[problem] = time

    # Loop through each drink and calculate the total time to solve all problems
    for drink, (problem, time) in drinks.items():
        problem_time[problem] += time

    # Return the total time to solve all problems for each drink
    return [problem_time[problem] for problem in problems]

