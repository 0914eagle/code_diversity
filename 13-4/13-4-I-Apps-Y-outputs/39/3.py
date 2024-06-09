
def solve(problems, drinks):
    # Initialize a dictionary to store the time it takes to solve each problem
    time_to_solve = {}

    # Iterate over each problem and calculate the time it takes to solve it
    for problem in problems:
        time_to_solve[problem] = problems[problem]

    # Iterate over each drink and calculate the time it takes to solve all problems if Joisino takes that drink
    for drink in drinks:
        for problem in problems:
            if problem in drinks[drink]:
                time_to_solve[problem] += drinks[drink][problem]

    # Return the time it takes to solve all problems for each drink
    return [time_to_solve[problem] for problem in problems]

