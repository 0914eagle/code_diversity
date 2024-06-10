
def is_interesting_problemset(problems, teams):
    # Initialize variables
    selected_problems = set()
    teams_with_knowledge = set()

    # Iterate through each problem
    for problem in problems:
        # Check if the problem is known by any team
        if any(team[problem] for team in teams):
            # Add the problem to the selected problems set
            selected_problems.add(problem)
            # Add the team to the set of teams with knowledge
            teams_with_knowledge.add(team for team in teams if team[problem])

    # Check if any team knows more than half of the selected problems
    if any(len(teams_with_knowledge) > len(selected_problems) / 2 for team in teams_with_knowledge):
        return "NO"

    return "YES"

def main():
    # Read the input
    n, k = map(int, input().split())
    problems = []
    for _ in range(n):
        problems.append(list(map(int, input().split())))

    # Call the function to check if the problemset is interesting
    result = is_interesting_problemset(problems, teams)

    # Print the result
    print(result)

if __name__ == '__main__':
    main()

