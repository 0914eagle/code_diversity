students_in_teams(n, k, skills):
    skills.sort()
    teams = [0] * k
    total_students = 0

    for skill in skills:
        min_team = min(teams)
        if min_team + 5 >= skill:
            teams[teams.index(min_team)] += 1
        else:
            teams[teams.index(0)] = 1

    total_students = sum(teams)
    return total_students

if __name__ == "__main__":
    n, k = map(int, input().split())
    skills = list(map(int, input().split()))
    result = max_students_in_teams(n, k, skills)
    print(result)    
