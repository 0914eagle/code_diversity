
def get_optimal_problems(problems, time_limit):
    # Sort the problems by the amount of time required to solve them
    sorted_problems = sorted(problems, key=lambda x: x[1])
    # Initialize the optimal set of problems to be empty
    optimal_set = []
    # Initialize the current time to 0
    current_time = 0
    # Iterate through the problems
    for problem in sorted_problems:
        # Check if solving the current problem will exceed the time limit
        if current_time + problem[1] > time_limit:
            # If it will, break the loop
            break
        # If not, add the problem to the optimal set
        optimal_set.append(problem)
        # Update the current time
        current_time += problem[1]
    # Return the optimal set of problems
    return optimal_set

def get_max_score(optimal_set, problems):
    # Initialize the maximum score to 0
    max_score = 0
    # Iterate through the optimal set of problems
    for problem in optimal_set:
        # Calculate the number of problems that can be solved before the current problem
        num_problems = sum(1 for p in problems if p[0] <= problem[0])
        # Check if the current problem can bring a point
        if num_problems <= problem[0]:
            # If it can, add 1 to the maximum score
            max_score += 1
    # Return the maximum score
    return max_score

def main():
    # Read the number of problems and the time limit from stdin
    n, time_limit = map(int, input().split())
    # Read the problems from stdin
    problems = [tuple(map(int, input().split())) for _ in range(n)]
    # Get the optimal set of problems
    optimal_set = get_optimal_problems(problems, time_limit)
    # Get the maximum score
    max_score = get_max_score(optimal_set, problems)
    # Print the maximum score
    print(max_score)
    # Print the number of problems to solve
    print(len(optimal_set))
    # Print the indexes of the problems to solve
    print(*[problem[2] for problem in optimal_set], sep=' ')

if __name__ == '__main__':
    main()

