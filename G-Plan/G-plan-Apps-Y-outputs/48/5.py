gn_teams(n, skills):
    teams = []
    skills.sort()
    for i in range(n):
        teams.append((skills[i], i % 3 + 1))
    return teams

def calculate_diversity(teams):
    total_diversity = 0
    team_diversities = [0, 0, 0]
    for skill, team in teams:
        team_diversities[team - 1] = max(team_diversities[team - 1], skill) - min(team_diversities[team - 1], skill)
    total_diversity = sum(team_diversities)
    return total_diversity

if __name__ == "__main__":
    n = int(input())
    skills = list(map(int, input().split()))
    
    teams = assign_teams(n, skills)
    total_diversity = calculate_diversity(teams)
    
    print(total_diversity, 3)
    for team in teams:
        print(team[1], end=' ')
