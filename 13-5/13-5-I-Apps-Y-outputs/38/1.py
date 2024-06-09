
def get_diversity(teams):
    diversity = 0
    for team in teams:
        diversity += max(team) - min(team)
    return diversity

def get_teams(students):
    teams = []
    while students:
        team = []
        while len(team) < 3:
            student = students.pop(0)
            team.append(student)
        teams.append(team)
    return teams

def get_optimal_teams(students):
    teams = get_teams(students)
    diversity = get_diversity(teams)
    optimal_teams = teams
    while True:
        teams = get_teams(students)
        if get_diversity(teams) < diversity:
            diversity = get_diversity(teams)
            optimal_teams = teams
        else:
            break
    return optimal_teams

def main():
    n = int(input())
    students = list(map(int, input().split()))
    teams = get_optimal_teams(students)
    print(get_diversity(teams), len(teams))
    for team in teams:
        print(*team)

if __name__ == '__main__':
    main()

