gn_teams(n, skills):
    teams = []
    skills.sort()
    for i in range(n):
        teams.append((skills[i], i % 3 + 1))
    return teams

def calculate_diversity(teams):
    diversity = 0
    for i in range(1, len(teams)):
        if teams[i][1] != teams[i - 1][1]:
            diversity += teams[i][0] - teams[i - 1][0]
    return diversity

if __name__ == "__main__":
    n = int(input())
    skills = list(map(int, input().split()))

    teams = assign_teams(n, skills)
    total_diversity = calculate_diversity(teams)

    team_count = max(team[1] for team in teams)
    print(total_diversity, team_count)
    for team in teams:
        print(team[1], end=' ')
