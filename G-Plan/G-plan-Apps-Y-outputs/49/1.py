students_in_teams(n, k, skills):
    skills.sort()
    teams = [[] for _ in range(k)]
    
    for skill in skills:
        min_team_idx = min(range(k), key=lambda i: len(teams[i]))
        if len(teams[min_team_idx]) == 0 or abs(skill - teams[min_team_idx][-1]) <= 5:
            teams[min_team_idx].append(skill)
    
    total_students = sum(len(team) for team in teams if team)
    return total_students

if __name__ == "__main__":
    n, k = map(int, input().split())
    skills = list(map(int, input().split()))
    result = max_students_in_teams(n, k, skills)
    print(result)
