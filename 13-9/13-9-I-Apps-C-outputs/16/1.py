
def check_interesting_problemset(problems, teams):
    # Initialize variables
    selected_problems = set()
    teams_knowing_problems = [set() for _ in range(len(teams))]

    # Loop through each problem and team
    for i in range(len(problems)):
        for j in range(len(teams)):
            # If the team knows the problem, add it to their set of known problems
            if teams[j][i] == 1:
                teams_knowing_problems[j].add(i)

    # Loop through each team and check if they know at most half of the selected problems
    for team in teams_knowing_problems:
        if len(team) > len(selected_problems) / 2:
            return "NO"

    return "YES"

def main():
    # Read input
    n, k = map(int, input().split())
    problems = [list(map(int, input().split())) for _ in range(n)]
    teams = [list(map(int, input().split())) for _ in range(k)]

    # Check if an interesting problemset can be made
    result = check_interesting_problemset(problems, teams)

    # Print output
    print(result)

if __name__ == '__main__':
    main()

