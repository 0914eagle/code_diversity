
def get_best_problems(problems, time_limit):
    # Sort the problems by the time it takes to solve them
    sorted_problems = sorted(problems, key=lambda x: x[1])
    # Initialize the best score and the list of problems to solve
    best_score = 0
    best_problems = []
    # Iterate through the problems and calculate the maximum score
    for problem in sorted_problems:
        # Check if the problem can be solved within the time limit
        if problem[1] <= time_limit:
            # Calculate the score for this problem
            score = 1
            for other_problem in sorted_problems:
                if other_problem != problem and other_problem[0] <= problem[0]:
                    score += 1
            # Check if the score is better than the current best score
            if score > best_score:
                # Update the best score and problems
                best_score = score
                best_problems = [problem[2]]
            # Check if the score is equal to the current best score
            elif score == best_score:
                # Add the problem to the list of problems
                best_problems.append(problem[2])
    return best_score, best_problems

def main():
    # Read the input
    n, time_limit = map(int, input().split())
    problems = []
    for i in range(n):
        a, t = map(int, input().split())
        problems.append((a, t, i+1))
    # Get the best problems
    score, problems = get_best_problems(problems, time_limit)
    # Print the output
    print(score)
    print(len(problems))
    print(*problems)

if __name__ == '__main__':
    main()

