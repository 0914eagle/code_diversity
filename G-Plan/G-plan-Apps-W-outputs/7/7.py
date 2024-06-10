_tank(tank, direction):
    return f"{tank} {direction}"

def rearrange_tanks(N, tanks):
    moves = []
    for i in range(N):
        while tanks[i][0] != i + 1 or tanks[i][1] != i + 1:
            if tanks[i][0] < i + 1:
                tanks[i][0] += 1
                moves.append(move_tank(i + 1, 'D'))
            elif tanks[i][0] > i + 1:
                tanks[i][0] -= 1
                moves.append(move_tank(i + 1, 'U'))
            elif tanks[i][1] < i + 1:
                tanks[i][1] += 1
                moves.append(move_tank(i + 1, 'R'))
            elif tanks[i][1] > i + 1:
                tanks[i][1] -= 1
                moves.append(move_tank(i + 1, 'L'))
    return moves

def main():
    N = int(input())
    tanks = [list(map(int, input().split())) for _ in range(N)]
    moves = rearrange_tanks(N, tanks)
    print(len(moves))
    for move in moves:
        print(move)

if __name__ == '__main__':
    main()
