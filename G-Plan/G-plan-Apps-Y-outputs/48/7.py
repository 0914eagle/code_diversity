gn_teams(n, skills):
    teams = []
    skills.sort()
    team_skills = [[] for _ in range(n)]
    for i in range(n):
        team_skills[i % 3].append(skills[i])
    total_diversity = sum(max(team) - min(team) for team in team_skills)
    return total_diversity, 3, [i % 3 + 1 for i in range(n)]

if __name__ == "__main__":
    n = int(input())
    skills = list(map(int, input().split()))
    res, k, team_assignments = assign_teams(n, skills)
    print(res, k)
    print(*team_assignments