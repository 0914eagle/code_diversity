
def solve(problems, drinks):
    # Initialize a dictionary to store the time it takes to solve each problem
    problem_time = {}
    for i in range(len(problems)):
        problem_time[i+1] = problems[i]

    # Initialize a list to store the time it takes to solve all problems if a drink is taken
    drink_time = []
    for i in range(len(drinks)):
        drink_time.append(0)
        for j in range(len(problems)):
            if j+1 == drinks[i][0]:
                drink_time[i] += drinks[i][1]
            else:
                drink_time[i] += problem_time[j+1]

    return drink_time

