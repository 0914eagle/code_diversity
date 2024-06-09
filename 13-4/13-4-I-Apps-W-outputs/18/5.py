
def get_players(n):
    return [i for i in range(1, n+1)]

def get_playing_fields(n, m):
    players = get_players(n)
    fields = []
    for i in range(m):
        field = [players[i], players[i+1]]
        fields.append(field)
    return fields

def get_assignment(n, m):
    fields = get_playing_fields(n, m)
    assignment = []
    for field in fields:
        assignment.append(str(field[0]) + " " + str(field[1]))
    return assignment

def main():
    n, m = map(int, input().split())
    assignment = get_assignment(n, m)
    for a in assignment:
        print(a)

if __name__ == '__main__':
    main()

