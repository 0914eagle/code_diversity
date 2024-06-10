
def get_input():
    n = int(input())
    stones = list(map(int, input().split()))
    matrix = []
    for i in range(n):
        matrix.append(list(input()))
    return n, stones, matrix

def get_moves(n, stones, matrix):
    moves = []
    for i in range(n):
        for j in range(i+1, n):
            if matrix[i][j] == matrix[stones[0]-1][stones[1]-1] and matrix[j][i] == matrix[stones[1]-1][stones[2]-1] and matrix[i][j] == matrix[stones[2]-1][stones[0]-1]:
                moves.append((stones[0], stones[1]))
                moves.append((stones[1], stones[2]))
                moves.append((stones[2], stones[0]))
                break
    return moves

def print_moves(moves):
    if len(moves) == 0:
        print(-1)
    else:
        print(len(moves))
        for move in moves:
            print(*move)

if __name__ == '__main__':
    n, stones, matrix = get_input()
    moves = get_moves(n, stones, matrix)
    print_moves(moves)

