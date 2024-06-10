
def read_input():
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
            if matrix[i][j] == matrix[stones[0]-1][stones[1]-1] and matrix[i][j] == matrix[stones[1]-1][stones[2]-1]:
                moves.append((i+1, j+1))
    return moves

def get_optimal_moves(n, stones, matrix):
    moves = get_moves(n, stones, matrix)
    if not moves:
        return -1
    return moves

def main():
    n, stones, matrix = read_input()
    moves = get_optimal_moves(n, stones, matrix)
    if moves == -1:
        print(-1)
    else:
        print(len(moves))
        for move in moves:
            print(move[0], move[1])

if __name__ == '__main__':
    main()

