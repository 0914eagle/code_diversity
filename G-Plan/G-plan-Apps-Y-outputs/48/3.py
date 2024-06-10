gn_teams(n, skills):
    teams = []
    skills.sort()
    for i in range(n):
        if i < 3:
            teams.append(1)
        else:
            teams.append(i % 3 + 1)
    return teams

def calculate_diversity(n, skills, teams):
    team_skills = [[] for _ in range(3)]
    for i in range(n):
        team_skills[teams[i] - 1].append(skills[i])
    
    total_diversity = 0
    for team in team_skills:
        diversity = max(team) - min(team)
        total_diversity += diversity
    
    return total_diversity

def minimize_diversity(n, skills):
    teams = assign_teams(n, skills)
    total_diversity = calculate_diversity(n, skills, teams)
    num_teams = len(set(teams))
    
    return total_diversity, num_teams, teams

if __name__ == "__main__":
    n = int(input())
    skills = list(map(int, input().split()))
    res, k, team_assignments = minimize_diversity(n, skills)
    print(res, k)
    print(*team_assignments)
