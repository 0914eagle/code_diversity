
def solve(problems, drinks):
    # Initialize a dictionary to store the time it takes to solve each problem
    problem_time = {}
    for problem in problems:
        problem_time[problem] = problems[problem]

    # Loop through each drink and calculate the time it takes to solve all problems
    for drink in drinks:
        # Initialize a variable to store the total time
        total_time = 0

        # Loop through each problem and calculate the time it takes to solve it with the current drink
        for problem in problems:
            if problem in drinks[drink]:
                total_time += drinks[drink][problem]
            else:
                total_time += problem_time[problem]

        # Print the total time it takes to solve all problems with the current drink
        print(total_time)

# Test the function with the sample input
solve({1: 2, 2: 1, 3: 4}, {1: {1: 1, 2: 1, 3: 3}, 2: {1: 2, 2: 3, 3: 4}})

