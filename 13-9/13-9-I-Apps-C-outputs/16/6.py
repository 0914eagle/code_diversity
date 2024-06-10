
def get_interesting_problemset(num_problems, num_teams, known_problems):
    # Initialize variables
    selected_problems = set()
    teams_with_known_problems = set()

    # Iterate over the known problems
    for team in known_problems:
        # Get the team's known problems
        team_problems = [problem for problem, is_known in enumerate(team) if is_known]

        # Add the team to the set of teams with known problems
        teams_with_known_problems.add(team)

        # Add the team's known problems to the selected problems set
        selected_problems.update(team_problems)

    # Check if it's possible to make an interesting problemset
    if len(selected_problems) >= num_problems // 2:
        return "YES"

    # Iterate over the remaining problems
    for problem in range(num_problems):
        # Check if the problem is not already selected
        if problem not in selected_problems:
            # Add the problem to the selected problems set
            selected_problems.add(problem)

            # Check if it's possible to make an interesting problemset with the current selected problems
            if len(selected_problems) >= num_problems // 2:
                return "YES"

            # Remove the problem from the selected problems set
            selected_problems.remove(problem)

    # If we reach this point, it's not possible to make an interesting problemset
    return "NO"

def main():
    # Read the input
    num_problems, num_teams = map(int, input().split())
    known_problems = [list(map(int, input().split())) for _ in range(num_problems)]

    # Call the get_interesting_problemset function
    result = get_interesting_problemset(num_problems, num_teams, known_problems)

    # Print the result
    print(result)

if __name__ == '__main__':
    main()

