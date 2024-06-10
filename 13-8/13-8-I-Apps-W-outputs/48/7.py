
def get_matrix_size():
    n, m, d = map(int, input().split())
    return n, m, d

def get_matrix(n, m):
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    return matrix

def get_min_moves(matrix, d):
    n, m = len(matrix), len(matrix[0])
    min_moves = 0
    for i in range(n):
        for j in range(m):
            min_moves += abs(matrix[i][j] - d)
    return min_moves

def main():
    n, m, d = get_matrix_size()
    matrix = get_matrix(n, m)
    min_moves = get_min_moves(matrix, d)
    print(min_moves)

if __name__ == '__main__':
    main()

