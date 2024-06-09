
def solve(N, T, M, P, X):
    # Initialize a list to store the time it takes to solve all problems
    time_taken = [0] * (M + 1)

    # Loop through each drink
    for i in range(1, M + 1):
        # Initialize a list to store the time it takes to solve each problem
        problem_time = [0] * (N + 1)

        # Loop through each problem
        for j in range(1, N + 1):
            # If the problem is not affected by the drink, use the original time
            if j not in P:
                problem_time[j] = T[j - 1]
            # Otherwise, use the modified time
            else:
                problem_time[j] = T[j - 1] + X[i - 1]

        # Calculate the total time it takes to solve all problems with the current drink
        time_taken[i] = sum(problem_time)

    return time_taken

