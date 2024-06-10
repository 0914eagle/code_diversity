
def get_optimal_problems(n, t, a, t_i):
    # Initialize the optimal set of problems to solve
    optimal_problems = []
    
    # Initialize the current time to 0
    current_time = 0
    
    # Iterate through the problems
    for i in range(n):
        # Check if the current problem can be solved within the time limit
        if current_time + t_i[i] <= t:
            # Add the problem to the optimal set of problems
            optimal_problems.append(i)
            # Update the current time
            current_time += t_i[i]
    
    # Return the optimal set of problems
    return optimal_problems

def get_optimal_score(n, a, optimal_problems):
    # Initialize the optimal score to 0
    optimal_score = 0
    
    # Iterate through the optimal problems
    for i in optimal_problems:
        # Check if the current problem can bring a point to the final score
        if a[i] >= len(optimal_problems) - 1:
            # Increment the optimal score
            optimal_score += 1
    
    # Return the optimal score
    return optimal_score

def main():
    # Read the input
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    t_i = list(map(int, input().split()))
    
    # Get the optimal set of problems to solve
    optimal_problems = get_optimal_problems(n, t, a, t_i)
    
    # Get the optimal score
    optimal_score = get_optimal_score(n, a, optimal_problems)
    
    # Print the output
    print(optimal_score)
    print(len(optimal_problems))
    print(*optimal_problems)

if __name__ == '__main__':
    main()

