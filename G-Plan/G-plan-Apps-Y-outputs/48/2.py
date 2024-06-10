gn_teams(n, skills):
    teams = []
    total_diversity = 0
    skills.sort()
    
    for i in range(n):
        teams.append(1)
    
    for i in range(3, n):
        total_diversity += skills[i] - skills[0]
    
    print(total_diversity, 1)
    print(*teams)

if __name__ == "__main__":
    n = int(input())
    skills = list(map(int, input().split()))
    assign_teams(n, skills)
