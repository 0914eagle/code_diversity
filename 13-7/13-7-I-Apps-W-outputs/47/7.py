
def get_optimal_problems(n, T, a, t):
    # Initialize the optimal set of problems to solve
    optimal_problems = []
    
    # Initialize the time required to solve the problems
    time_required = 0
    
    # Iterate over the problems
    for i in range(n):
        # Check if solving the current problem will not exceed the time limit
        if time_required + t[i] <= T:
            # Add the current problem to the optimal set of problems
            optimal_problems.append(i)
            # Update the time required to solve the problems
            time_required += t[i]
    
    # Return the optimal set of problems
    return optimal_problems

def get_optimal_score(n, T, a, t, optimal_problems):
    # Initialize the optimal score to 0
    optimal_score = 0
    
    # Iterate over the optimal problems
    for i in optimal_problems:
        # Check if the current problem will bring a point to the score
        if a[i] >= len(optimal_problems) - 1:
            # Add 1 to the optimal score
            optimal_score += 1
    
    # Return the optimal score
    return optimal_score

def main():
    # Read the input
    n, T = map(int, input().split())
    a = list(map(int, input().split()))
    t = list(map(int, input().split()))
    
    # Get the optimal set of problems to solve
    optimal_problems = get_optimal_problems(n, T, a, t)
    
    # Get the optimal score
    optimal_score = get_optimal_score(n, T, a, t, optimal_problems)
    
    # Print the optimal score and the optimal set of problems
    print(optimal_score)
    print(len(optimal_problems))
    print(*optimal_problems)

if __name__ == '__main__':
    main()

