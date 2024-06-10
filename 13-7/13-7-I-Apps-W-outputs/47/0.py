
def get_max_score(problems, time_limit):
    # Sort the problems by the time it takes to solve them in descending order
    sorted_problems = sorted(problems, key=lambda x: x[1], reverse=True)
    
    # Initialize the maximum score and the list of problems to solve
    max_score = 0
    problems_to_solve = []
    
    # Iterate through the problems and calculate the maximum score
    for problem in sorted_problems:
        # Check if the problem can be solved within the time limit
        if problem[1] <= time_limit:
            # Add the problem to the list of problems to solve
            problems_to_solve.append(problem[0])
            # Update the maximum score
            max_score += problem[0]
            # Update the time limit
            time_limit -= problem[1]
    
    return max_score, problems_to_solve

def main():
    # Read the input
    n, time_limit = map(int, input().split())
    problems = []
    for _ in range(n):
        a, t = map(int, input().split())
        problems.append((a, t))
    
    # Get the maximum score and the list of problems to solve
    max_score, problems_to_solve = get_max_score(problems, time_limit)
    
    # Print the output
    print(max_score)
    print(len(problems_to_solve))
    print(*problems_to_solve)

if __name__ == '__main__':
    main()

