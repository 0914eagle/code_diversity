
def get_teammate(strengths):
    n = len(strengths)
    teammates = [0] * n
    for i in range(n):
        max_strength = 0
        for j in range(n):
            if i != j and strengths[i][j] > max_strength:
                max_strength = strengths[i][j]
                teammates[i] = j
    return teammates

def get_teams(teammates):
    n = len(teammates)
    teams = []
    for i in range(n):
        team = [i, teammates[i]]
        teams.append(team)
    return teams

def main():
    n = int(input())
    strengths = []
    for i in range(n):
        strengths.append(list(map(int, input().split())))
    teammates = get_teammate(strengths)
    teams = get_teams(teammates)
    print(*teammates, sep=' ')
    print(*teams, sep='\n')

if __name__ == '__main__':
    main()

