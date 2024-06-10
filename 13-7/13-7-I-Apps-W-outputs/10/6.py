
def read_input():
    n = int(input())
    stones = [int(i) for i in input().split()]
    matrix = []
    for i in range(n):
        matrix.append(input())
    return n, stones, matrix

def get_moves(n, stones, matrix):
    moves = []
    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j] == matrix[stones[0]][stones[1]] and matrix[j][stones[2]] == matrix[stones[0]][stones[1]]:
                moves.append((i, j))
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

