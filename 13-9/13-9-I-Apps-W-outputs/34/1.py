
def get_teammates(n, strengths):
    teammates = [-1] * (n + 1)
    for i in range(1, n + 1):
        max_strength = -1
        for j in range(1, n + 1):
            if i != j and strengths[i][j] > max_strength:
                max_strength = strengths[i][j]
                teammates[i] = j
    return teammates

def get_team_strengths(n, teammates):
    team_strengths = [0] * (n + 1)
    for i in range(1, n + 1):
        team_strengths[i] = teammates[i]
    return team_strengths

def main():
    n = int(input())
    strengths = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        strengths[i] = list(map(int, input().split()))
    teammates = get_teammates(n, strengths)
    team_strengths = get_team_strengths(n, teammates)
    print(*team_strengths, sep='\n')

if __name__ == '__main__':
    main()

