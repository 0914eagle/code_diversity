
def get_maximum_score(problems, time_limit):
    # Sort the problems by their value (a_i) in descending order
    problems.sort(key=lambda x: x[0], reverse=True)
    # Initialize the maximum score and the chosen problems
    max_score = 0
    chosen_problems = []
    # Iterate through the problems
    for problem in problems:
        # Check if the problem can be solved within the time limit
        if problem[1] <= time_limit:
            # Add the problem to the chosen problems
            chosen_problems.append(problem[0])
            # Update the maximum score
            max_score += problem[0]
            # Update the time limit
            time_limit -= problem[1]
    # Return the maximum score and the chosen problems
    return max_score, chosen_problems

def main():
    # Read the input
    n, time_limit = map(int, input().split())
    problems = []
    for _ in range(n):
        a, t = map(int, input().split())
        problems.append((a, t))
    # Get the maximum score and the chosen problems
    max_score, chosen_problems = get_maximum_score(problems, time_limit)
    # Print the output
    print(max_score)
    print(len(chosen_problems))
    print(*chosen_problems)

if __name__ == '__main__':
    main()

