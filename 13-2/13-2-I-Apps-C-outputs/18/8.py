
def is_interesting_problemset(problems, teams):
    # Calculate the maximum number of problems that each team can know
    max_problems = len(problems) // 2

    # Initialize a set to store the problems that each team knows
    team_problems = [set() for _ in range(len(teams))]

    # Loop through each problem and team to check if the team knows the problem
    for i, problem in enumerate(problems):
        for j, team in enumerate(teams):
            if team[i] == 1:
                team_problems[j].add(i)

    # Check if any team knows more than the maximum number of problems allowed
    for team in team_problems:
        if len(team) > max_problems:
            return "NO"

    # If we reach this point, it means that each team knows at most half of the problems
    return "YES"

