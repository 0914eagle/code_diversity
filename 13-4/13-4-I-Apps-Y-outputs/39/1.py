
def solve(N, T, M, P, X):
    # Initialize a list to store the time it takes to solve all problems
    time_taken = []
    
    # Loop through each drink
    for i in range(M):
        # Initialize a list to store the time it takes to solve each problem
        problem_time = []
        
        # Loop through each problem
        for j in range(N):
            # If the problem is not the one that is stimulated by the drink
            if j != P[i]:
                # Add the time it takes to solve the problem to the list
                problem_time.append(T[j])
            else:
                # Add the stimulated time to the list
                problem_time.append(X[i])
                
        # Calculate the total time it takes to solve all problems
        total_time = sum(problem_time)
        
        # Add the total time to the list of times taken
        time_taken.append(total_time)
    
    return time_taken

