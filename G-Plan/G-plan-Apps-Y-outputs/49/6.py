students_in_teams(n, k, skills):
    skills.sort()
    teams = []
    for skill in skills:
        assigned = False
        for team in teams:
            if abs(skill - team[-1]) <= 5:
                team.append(skill)
                assigned = True
                break
        if not assigned:
            teams.append([skill])
    
    total_students = sum(len(team) for team in teams)
    return min(total_students, k * len(teams))

if __name__ == "__main__":
    n, k = map(int, input().split())
    skills = list(map(int, input().split()))
    result = max_students_in_teams(n, k, skills)
    print(result)
