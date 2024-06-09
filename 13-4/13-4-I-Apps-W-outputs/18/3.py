
def f1(N, M):
    # Initialize the playing fields with random integers between 1 and N
    fields = [(i, random.randint(1, N)) for i in range(1, M+1)]
    # Assign each player a unique integer between 1 and N
    players = list(range(1, N+1))
    # Shuffle the players to randomize the order
    random.shuffle(players)
    # Assign each player to a playing field
    for i in range(M):
        fields[i] = (fields[i][0], players[i-1])
    return fields

def f2(N, M):
    # Initialize the playing fields with random integers between 1 and N
    fields = [(i, random.randint(1, N)) for i in range(1, M+1)]
    # Assign each player a unique integer between 1 and N
    players = list(range(1, N+1))
    # Shuffle the players to randomize the order
    random.shuffle(players)
    # Assign each player to a playing field
    for i in range(M):
        fields[i] = (fields[i][0], players[i-1])
    return fields

if __name__ == '__main__':
    N, M = map(int, input().split())
    fields = f1(N, M)
    for field in fields:
        print(field[0], field[1])

