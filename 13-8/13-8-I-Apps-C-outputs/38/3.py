
def get_input():
    n, k = map(int, input().split())
    players = []
    for _ in range(n):
        players.append(list(map(int, input().split())))
    return n, k, players

def get_similarity(player, new_player):
    similarity = 0
    for i in range(len(player)):
        if player[i] == new_player[i]:
            similarity += 1
    return similarity

def get_new_player(n, k, players):
    new_player = [0] * k
    max_similarity = 0
    for i in range(1 << k):
        player = list(bin(i)[2:].zfill(k))
        similarity = 0
        for p in players:
            similarity += get_similarity(p, player)
        if similarity > max_similarity:
            max_similarity = similarity
            new_player = player
    return new_player

def main():
    n, k, players = get_input()
    new_player = get_new_player(n, k, players)
    print(*new_player)

if __name__ == '__main__':
    main()

