
def max_students_teams(n, k, skills):
    skills.sort()
    teams = [0] * k
    total_students = 0

    for skill in skills:
        min_team_idx = min(range(k), key=lambda i: teams[i])
        if teams[min_team_idx] == 0 or abs(skill - teams[min_team_idx]) <= 5:
            teams[min_team_idx] = skill
            total_students += 1

    return total_students

if __name__ == "__main__":
    n, k = map(int, input().split())
    skills = list(map(int, input().split()))
    result = max_students_teams(n, k, skills)
    print(result)
