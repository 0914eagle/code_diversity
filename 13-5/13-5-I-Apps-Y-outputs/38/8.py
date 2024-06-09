
def get_diversity(team):
    return max(team) - min(team)

def get_teams(students, k):
    teams = []
    for i in range(k):
        teams.append([])
    for i, student in enumerate(students):
        teams[i % k].append(student)
    return teams

def get_total_diversity(teams):
    return sum([get_diversity(team) for team in teams])

def get_optimal_teams(students):
    n = len(students)
    if n == 3:
        return [students]
    elif n == 4:
        return [[students[0], students[1], students[2]], [students[0], students[1], students[3]]]
    elif n == 5:
        return [[students[0], students[1], students[2]], [students[0], students[1], students[4]], [students[0], students[2], students[3]], [students[1], students[2], students[3], students[4]]]
    elif n == 6:
        return [[students[0], students[1], students[2]], [students[0], students[1], students[5]], [students[0], students[2], students[3]], [students[0], students[2], students[4]], [students[1], students[2], students[3], students[4], students[5]]]
    else:
        teams = []
        for i in range(n // 3):
            teams.append([students[i], students[n // 3 + i], students[2 * n // 3 + i]])
        for i in range(n % 3):
            teams[-1].append(students[n - 1 - i])
        return teams

def solve(students):
    n = len(students)
    if n <= 3:
        return [students]
    else:
        teams = get_optimal_teams(students)
        return teams

def main():
    n = int(input())
    students = list(map(int, input().split()))
    teams = solve(students)
    print(get_total_diversity(teams))
    print(*[team[0] for team in teams])

if __name__ == '__main__':
    main()

