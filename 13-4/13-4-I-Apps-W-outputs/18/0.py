
def get_players(n):
    return [i for i in range(1, n+1)]

def get_playing_fields(m, n):
    fields = []
    for i in range(m):
        a = i % n + 1
        b = (i + 1) % n + 1
        fields.append((a, b))
    return fields

def get_next_players(players, n):
    next_players = []
    for i in range(n):
        next_players.append((players[i] + 1) % n + 1)
    return next_players

def get_assignment(m, n):
    players = get_players(n)
    fields = get_playing_fields(m, n)
    for i in range(n):
        fields[i] = (players[i], players[(i+1) % n])
    return fields

def main():
    n, m = map(int, input().split())
    fields = get_assignment(m, n)
    for field in fields:
        print(*field)

if __name__ == '__main__':
    main()

