
def get_interesting_problemset(n, k, team_knowledge):
    # Initialize variables
    selected_problems = set()
    teams_with_known_problems = [set() for _ in range(k)]

    # Iterate over the teams and their known problems
    for i, team in enumerate(team_knowledge):
        for j, known in enumerate(team):
            if known:
                teams_with_known_problems[i].add(j)

    # Iterate over the problems
    for i in range(n):
        # Check if the problem is known by at least half of the teams
        if len(teams_with_known_problems[i]) >= k // 2:
            # Add the problem to the selected problems
            selected_problems.add(i)

    # Check if the selected problems form an interesting problemset
    if len(selected_problems) >= k // 2:
        return "YES"
    else:
        return "NO"

def main():
    n, k = map(int, input().split())
    team_knowledge = [list(map(int, input().split())) for _ in range(n)]
    print(get_interesting_problemset(n, k, team_knowledge))

if __name__ == '__main__':
    main()

