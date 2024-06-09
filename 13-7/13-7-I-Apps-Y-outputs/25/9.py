
def solve(problems, drinks):
    # Initialize a dictionary to store the time it takes to solve each problem
    problem_time = {}
    for problem in problems:
        problem_time[problem] = problems[problem]

    # Initialize a list to store the time it takes to solve all problems if a drink is taken
    drink_time = []

    # Loop through each drink and calculate the time it takes to solve all problems
    for drink in drinks:
        for problem in problems:
            if problem in drinks[drink]:
                problem_time[problem] = drinks[drink][problem]
        drink_time.append(sum(problem_time.values()))

    return drink_time

