
def read_input():
    n = int(input())
    vertices = [int(x) for x in input().split()]
    matrix = []
    for i in range(n):
        matrix.append(list(input()))
    return n, vertices, matrix

def get_moves(n, vertices, matrix):
    moves = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == matrix[vertices[0]-1][vertices[1]-1] and matrix[i][j] == matrix[vertices[1]-1][vertices[2]-1]:
                moves.append((i+1, j+1))
    return moves

def play_game(n, vertices, matrix):
    moves = get_moves(n, vertices, matrix)
    if not moves:
        return -1
    return len(moves), moves

def main():
    n, vertices, matrix = read_input()
    result = play_game(n, vertices, matrix)
    if result == -1:
        print(-1)
    else:
        print(result[0])
        for move in result[1]:
            print(move[0], move[1])

if __name__ == '__main__':
    main()

