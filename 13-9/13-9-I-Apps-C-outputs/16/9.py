
def get_interesting_problemset(n, k, team_problems):
    # Initialize a set to store the selected problems
    selected_problems = set()

    # Iterate over the teams
    for team in team_problems:
        # Get the problems known by the current team
        team_problems_set = set(team)

        # If the current team knows some problems, add them to the selected problems set
        if len(team_problems_set) > 0:
            selected_problems = selected_problems.union(team_problems_set)

    # Check if the selected problems set is at most half of the total number of problems
    if len(selected_problems) <= n // 2:
        return "YES"
    else:
        return "NO"

def main():
    # Read the input
    n, k = map(int, input().split())
    team_problems = [list(map(int, input().split())) for _ in range(n)]

    # Call the get_interesting_problemset function and print the result
    result = get_interesting_problemset(n, k, team_problems)
    print(result)

if __name__ == '__main__':
    main()

