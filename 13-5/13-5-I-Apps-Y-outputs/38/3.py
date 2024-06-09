
def get_diversity(team):
    return max(team) - min(team)

def get_teams(students):
    teams = []
    for i in range(0, len(students), 3):
        team = students[i:i+3]
        teams.append(team)
    return teams

def get_total_diversity(teams):
    return sum([get_diversity(team) for team in teams])

def get_optimal_teams(students):
    teams = get_teams(students)
    total_diversity = get_total_diversity(teams)
    for i in range(len(students)):
        for j in range(i+1, len(students)):
            for k in range(j+1, len(students)):
                team = [students[i], students[j], students[k]]
                if get_diversity(team) < total_diversity:
                    teams = get_teams(team)
                    total_diversity = get_total_diversity(teams)
    return teams

def main():
    n = int(input())
    students = list(map(int, input().split()))
    teams = get_optimal_teams(students)
    print(total_diversity, len(teams))
    for team in teams:
        print(*team)

if __name__ == '__main__':
    main()

