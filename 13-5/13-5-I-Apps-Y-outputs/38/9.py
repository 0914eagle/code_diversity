
def get_diversity(team):
    return max(team) - min(team)

def get_teams(students):
    teams = []
    while students:
        team = [students.pop()]
        while len(team) < 3:
            min_diff = float('inf')
            min_index = -1
            for i, student in enumerate(students):
                diff = abs(student - team[0])
                if diff < min_diff:
                    min_diff = diff
                    min_index = i
            team.append(students.pop(min_index))
        teams.append(team)
    return teams

def get_total_diversity(teams):
    return sum(get_diversity(team) for team in teams)

def get_optimal_teams(students):
    teams = get_teams(students)
    return teams, get_total_diversity(teams)

if __name__ == '__main__':
    n = int(input())
    students = sorted(list(map(int, input().split())))
    teams, total_diversity = get_optimal_teams(students)
    print(total_diversity, len(teams))
    for team in teams:
        print(*team)

