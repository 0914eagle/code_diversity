students_in_teams(n, k, skills):
    skills.sort()
    teams = [0] * k
    for skill in skills:
        min_team_size = min(teams)
        idx = teams.index(min_team_size)
        if abs(skill - min_team_size) <= 5:
            teams[idx] += 1
    return sum(teams)

if __name__ == "__main__":
    n, k = map(int, input().split())
    skills = list(map(int, input().split()))
    print(max_students_in_teams(n, k, skills)