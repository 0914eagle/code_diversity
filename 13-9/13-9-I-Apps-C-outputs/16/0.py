
def is_interesting_problemset(problem_bank, teams):
    # Initialize variables
    num_problems = len(problem_bank)
    num_teams = len(teams)
    team_knows_problem = [[0] * num_problems for _ in range(num_teams)]

    # Fill in the team_knows_problem matrix
    for i, team in enumerate(teams):
        for j, knows_problem in enumerate(team):
            if knows_problem:
                team_knows_problem[i][j] = 1

    # Check if it is possible to make an interesting problemset
    for i in range(num_problems):
        num_teams_knowing_problem = 0
        for j in range(num_teams):
            if team_knows_problem[j][i]:
                num_teams_knowing_problem += 1
        if num_teams_knowing_problem > num_teams / 2:
            return False

    return True

def main():
    num_problems, num_teams = map(int, input().split())
    problem_bank = [int(i) for i in input().split()]
    teams = []
    for _ in range(num_teams):
        teams.append([int(i) for i in input().split()])
    if is_interesting_problemset(problem_bank, teams):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

