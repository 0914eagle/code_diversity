
def get_spread(player_pieces):
    spread = 0
    for i in range(len(player_pieces)):
        for j in range(i+1, len(player_pieces)):
            spread += get_distance(player_pieces[i], player_pieces[j])
    return spread

def get_distance(piece1, piece2):
    row1, col1 = piece1
    row2, col2 = piece2
    return abs(row1 - row2) + abs(col1 - col2)

def main():
    R, C = map(int, input().split())
    player_pieces = []
    for _ in range(R):
        row = list(input())
        for i in range(C):
            if row[i] == 'M':
                player_pieces.append((i, _))
    spread = get_spread(player_pieces)
    print(spread)

if __name__ == '__main__':
    main()

