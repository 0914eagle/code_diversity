
def get_diversity(team):
    return max(team) - min(team)

def get_teams(students):
    teams = []
    while students:
        team = [students.pop()]
        while len(team) < 3 and students:
            team.append(students.pop())
        teams.append(team)
    return teams

def get_total_diversity(teams):
    return sum(get_diversity(team) for team in teams)

def get_optimal_teams(students):
    teams = get_teams(students)
    return teams, get_total_diversity(teams)

def main():
    n = int(input())
    students = list(map(int, input().split()))
    teams, total_diversity = get_optimal_teams(students)
    print(total_diversity, len(teams))
    for team in teams:
        print(*team)

if __name__ == '__main__':
    main()

