de_students(n, skills):
    skills.sort()
    teams = [[] for _ in range(n)]
    total_diversity = 0
    team_diversity = [0] * n

    for i in range(n):
        teams[i % 3].append(i)
    
    for team in teams:
        team_skills = [skills[i] for i in team]
        team_diversity = max(team_skills) - min(team_skills)
        total_diversity += team_diversity

    return total_diversity, len(teams), teams

if __name__ == "__main__":
    n = int(input())
    skills = list(map(int, input().split()))

    res, k, teams = divide_students(n, skills)
    print(res, k)
    for team in teams:
        for student in team:
            print(team.index(student) + 1, end=" ")
        print()
