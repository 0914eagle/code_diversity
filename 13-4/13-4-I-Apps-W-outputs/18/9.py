
def get_players(n):
    return [i for i in range(1, n+1)]

def get_playing_fields(m, n):
    players = get_players(n)
    fields = []
    for i in range(m):
        field = [players[i], players[i+1]]
        fields.append(field)
    return fields

def get_assignment(n, m):
    fields = get_playing_fields(m, n)
    assignment = []
    for field in fields:
        assignment.append(field)
    return assignment

def main():
    n, m = map(int, input().split())
    assignment = get_assignment(n, m)
    for field in assignment:
        print(*field)

if __name__ == '__main__':
    main()

