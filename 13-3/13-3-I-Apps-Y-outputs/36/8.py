
def f1(W, H, map):
    # Initialize variables
    gold_count = 0
    trap_count = 0
    player_position = []
    safe_squares = []

    # Parse the map
    for i in range(H):
        for j in range(W):
            if map[i][j] == 'P':
                player_position = [i, j]
            elif map[i][j] == 'G':
                gold_count += 1
            elif map[i][j] == 'T':
                trap_count += 1
            elif map[i][j] == '#':
                continue
            else:
                safe_squares.append([i, j])

    # Find the safe squares that are next to the player's position
    for i in range(len(safe_squares)):
        if safe_squares[i][0] == player_position[0] and safe_squares[i][1] == player_position[1] + 1:
            safe_squares.pop(i)
        elif safe_squares[i][0] == player_position[0] and safe_squares[i][1] == player_position[1] - 1:
            safe_squares.pop(i)
        elif safe_squares[i][0] == player_position[0] + 1 and safe_squares[i][1] == player_position[1]:
            safe_squares.pop(i)
        elif safe_squares[i][0] == player_position[0] - 1 and safe_squares[i][1] == player_position[1]:
            safe_squares.pop(i)

    # Calculate the number of gold the player can get safely
    gold_count_safe = gold_count - trap_count

    return gold_count_safe

def f2(W, H, map):
    # Initialize variables
    gold_count = 0
    trap_count = 0
    player_position = []
    safe_squares = []

    # Parse the map
    for i in range(H):
        for j in range(W):
            if map[i][j] == 'P':
                player_position = [i, j]
            elif map[i][j] == 'G':
                gold_count += 1
            elif map[i][j] == 'T':
                trap_count += 1
            elif map[i][j] == '#':
                continue
            else:
                safe_squares.append([i, j])

    # Find the safe squares that are next to the player's position
    for i in range(len(safe_squares)):
        if safe_squares[i][0] == player_position[0] and safe_squares[i][1] == player_position[1] + 1:
            safe_squares.pop(i)
        elif safe_squares[i][0] == player_position[0] and safe_squares[i][1] == player_position[1] - 1:
            safe_squares.pop(i)
        elif safe_squares[i][0] == player_position[0] + 1 and safe_squares[i][1] == player_position[1]:
            safe_squares.pop(i)
        elif safe_squares[i][0] == player_position[0] - 1 and safe_squares[i][1] == player_position[1]:
            safe_squares.pop(i)

    # Calculate the number of gold the player can get safely
    gold_count_safe = gold_count - trap_count

    return gold_count_safe

if __name__ == '__main__':
    W, H = map(int, input().split())
    map = []
    for i in range(H):
        map.append(list(input()))
    print(f1(W, H, map))
    print(f2(W, H, map))

