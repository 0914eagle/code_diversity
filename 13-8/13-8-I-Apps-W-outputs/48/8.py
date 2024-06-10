
def get_matrix_size():
    n, m, d = map(int, input().split())
    return n, m, d

def get_matrix():
    n, m = get_matrix_size()
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    return matrix

def get_moves(matrix, d):
    n, m = get_matrix_size()
    moves = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] % d != 0:
                moves += matrix[i][j] % d
                matrix[i][j] -= matrix[i][j] % d
    return moves

def main():
    matrix = get_matrix()
    d = get_matrix_size()[2]
    moves = get_moves(matrix, d)
    print(moves)

if __name__ == '__main__':
    main()

