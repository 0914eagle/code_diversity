
def get_diversity(teams):
    diversity = 0
    for team in teams:
        diversity += max(team) - min(team)
    return diversity

def form_teams(students, k):
    teams = []
    for i in range(k):
        teams.append([])
    for i, skill in enumerate(students):
        teams[i % k].append(skill)
    return teams

def get_optimal_teams(students):
    n = len(students)
    k = 1
    while k <= n // 3:
        teams = form_teams(students, k)
        if get_diversity(teams) < get_diversity(teams[:k]):
            break
        k += 1
    return teams[:k]

def main():
    n = int(input())
    students = list(map(int, input().split()))
    teams = get_optimal_teams(students)
    print(get_diversity(teams), len(teams))
    for team in teams:
        print(*team)

if __name__ == '__main__':
    main()

