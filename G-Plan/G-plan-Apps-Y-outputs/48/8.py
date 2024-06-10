gn_teams(n, skills):
    teams = []
    skills_sorted = sorted(enumerate(skills), key=lambda x: x[1])
    
    for i in range(n):
        teams.append((i % 3) + 1)
    
    return teams

if __name__ == "__main__":
    n = int(input())
    skills = list(map(int, input().split()))
    
    teams = assign_teams(n, skills)
    total_diversity = max(skills) - min(skills)
    
    print(total_diversity, max(teams))
    print(*teams