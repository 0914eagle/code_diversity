
def solve(problems, drinks):
    # Initialize a dictionary to store the time it takes to solve each problem
    problem_time = {}
    for i, time in enumerate(problems, start=1):
        problem_time[i] = time

    # Iterate through each drink and calculate the total time to solve all problems
    for drink in drinks:
        total_time = 0
        for problem, time in problem_time.items():
            if problem in drink:
                total_time += drink[1]
            else:
                total_time += time
        print(total_time)

# Test the function with the sample input
solve([2, 1, 4], [[1, 1], [2, 3]])

