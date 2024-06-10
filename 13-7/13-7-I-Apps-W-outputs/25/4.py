
def get_team_counts(teams):
    team_counts = {}
    for team in teams:
        if team not in team_counts:
            team_counts[team] = 1
        else:
            team_counts[team] += 1
    return team_counts

def get_min_switches(team_counts):
    min_switches = 0
    for team, count in team_counts.items():
        if count > 1:
            min_switches += count - 1
    return min_switches

def solve(n, teams):
    team_counts = get_team_counts(teams)
    return get_min_switches(team_counts)

if __name__ == '__main__':
    n = int(input())
    teams = input()
    print(solve(n, teams))

