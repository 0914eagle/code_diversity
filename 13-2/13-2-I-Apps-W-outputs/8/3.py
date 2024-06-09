
def get_home_away_games(n, teams):
    home_games = 0
    away_games = 0
    for i in range(n):
        for j in range(i+1, n):
            if teams[i][0] != teams[j][0] and teams[i][1] != teams[j][1]:
                home_games += 1
                away_games += 1
            elif teams[i][0] != teams[j][0] or teams[i][1] != teams[j][1]:
                home_games += 1
                away_games += 1
    return [home_games, away_games]

def main():
    n = int(input())
    teams = []
    for i in range(n):
        teams.append(list(map(int, input().split())))
    home_away_games = get_home_away_games(n, teams)
    print(*home_away_games)

if __name__ == '__main__':
    main()

