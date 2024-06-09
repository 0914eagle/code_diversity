
def get_players(n):
    return [i for i in range(1, n+1)]

def get_fields(m, n):
    fields = []
    for i in range(m):
        fields.append([i%n+1, (i+1)%n+1])
    return fields

def get_players_per_field(fields, players):
    players_per_field = []
    for field in fields:
        players_per_field.append([players[field[0]-1], players[field[1]-1]])
    return players_per_field

def get_unique_players(players_per_field):
    unique_players = []
    for field in players_per_field:
        if field[0] not in unique_players:
            unique_players.append(field[0])
        if field[1] not in unique_players:
            unique_players.append(field[1])
    return unique_players

def get_assignment(n, m):
    players = get_players(n)
    fields = get_fields(m, n)
    players_per_field = get_players_per_field(fields, players)
    unique_players = get_unique_players(players_per_field)
    return unique_players

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(*get_assignment(n, m), sep='\n')

