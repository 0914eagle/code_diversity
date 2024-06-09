
def solve(problems, drinks):
    # Initialize a dictionary to store the time it takes to solve each problem
    problem_time = {}
    for problem in problems:
        problem_time[problem] = problems[problem]

    # Loop through each drink and calculate the time it takes to solve all problems
    for drink in drinks:
        for problem in problems:
            if problem in drinks[drink]:
                problem_time[problem] += drinks[drink]

    # Return the time it takes to solve all problems for each drink
    return [problem_time[problem] for problem in problems]

