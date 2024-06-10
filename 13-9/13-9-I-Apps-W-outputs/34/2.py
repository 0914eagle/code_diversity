
def get_teammate(n, strength):
    teammates = [-1] * (n + 1)
    for i in range(1, n + 1):
        max_strength = 0
        for j in range(1, n + 1):
            if i != j and strength[i][j] > max_strength:
                max_strength = strength[i][j]
                teammates[i] = j
    return teammates

def get_team_strength(n, strength, teammates):
    team_strength = [0] * (n + 1)
    for i in range(1, n + 1):
        team_strength[i] = strength[i][teammates[i]]
    return team_strength

def get_max_team_strength(n, strength):
    teammates = get_teammate(n, strength)
    team_strength = get_team_strength(n, strength, teammates)
    return max(team_strength)

def main():
    n = int(input())
    strength = []
    for i in range(n):
        strength.append(list(map(int, input().split())))
    print(*get_teammate(n, strength))

if __name__ == '__main__':
    main()

