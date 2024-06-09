
def get_diversity(teams):
    diversity = 0
    for team in teams:
        diversity += max(team) - min(team)
    return diversity

def form_teams(students):
    teams = []
    while students:
        team = []
        for _ in range(3):
            team.append(students.pop())
        teams.append(team)
    return teams

def get_optimal_teams(students):
    teams = form_teams(students)
    diversity = get_diversity(teams)
    optimal_teams = teams
    while True:
        for i in range(len(teams)):
            for j in range(i+1, len(teams)):
                team1 = teams[i]
                team2 = teams[j]
                team1.extend(team2)
                team2 = []
                teams[i] = team1
                teams[j] = team2
                diversity_new = get_diversity(teams)
                if diversity_new < diversity:
                    diversity = diversity_new
                    optimal_teams = teams
        if not any(teams):
            break
    return optimal_teams

def main():
    n = int(input())
    students = list(map(int, input().split()))
    teams = get_optimal_teams(students)
    print(get_diversity(teams))
    print(len(teams))
    for team in teams:
        print(*team)

if __name__ == '__main__':
    main()

