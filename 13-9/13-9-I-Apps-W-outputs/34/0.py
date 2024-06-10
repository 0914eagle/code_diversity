
def get_team_strength(teams, team_size):
    team_strength = []
    for team in teams:
        team_strength.append(max(team))
    return team_strength

def get_teammates(team_strength, team_size):
    teammates = []
    for i in range(team_size):
        teammates.append(team_strength.index(max(team_strength)) + 1)
        team_strength[team_strength.index(max(team_strength))] = 0
    return teammates

def main():
    team_size = int(input())
    teams = []
    for i in range(team_size):
        teams.append(list(map(int, input().split())))
    team_strength = get_team_strength(teams, team_size)
    teammates = get_teammates(team_strength, team_size)
    print(*teammates)

if __name__ == '__main__':
    main()

