de_students(n, skills):
    teams = []
    total_diversity = 0
    skills.sort()
    
    for i in range(3):
        teams.append([])
    
    for skill in skills:
        min_diversity = float('inf')
        min_team = -1
        
        for j in range(3):
            diversity = teams[j][-1] - teams[j][0] if teams[j] else 0
            
            if diversity < min_diversity:
                min_diversity = diversity
                min_team = j
        
        teams[min_team].append(skill)
    
    for team in teams:
        total_diversity += team[-1] - team[0]
    
    return total_diversity, len(teams), [min(i+1, 3) for i in sum([[idx]*len(team) for idx, team in enumerate(teams)], [])]

if __name__ == "__main__":
    n = int(input())
    skills = list(map(int, input().split()))
    res, k, team_assignments = divide_students(n, skills)
    print(res, k)
    print(" ".join(map(str, team_assignments)