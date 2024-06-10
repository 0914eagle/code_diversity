
def check_interesting_problemset(problems, teams):
    # Initialize variables
    num_problems = len(problems)
    num_teams = len(teams)
    team_problems = [set() for _ in range(num_teams)]

    # Build a set of problems known by each team
    for i, team in enumerate(teams):
        for j, problem in enumerate(team):
            if problem == 1:
                team_problems[i].add(j)

    # Check if it is possible to make an interesting problemset
    for i in range(num_problems):
        problem_teams = set()
        for j in range(num_teams):
            if i in team_problems[j]:
                problem_teams.add(j)
        if len(problem_teams) > num_teams // 2:
            return "NO"

    return "YES"

def main():
    num_problems, num_teams = map(int, input().split())
    problems = [list(map(int, input().split())) for _ in range(num_problems)]
    teams = [list(map(int, input().split())) for _ in range(num_teams)]
    print(check_interesting_problemset(problems, teams))

if __name__ == '__main__':
    main()

