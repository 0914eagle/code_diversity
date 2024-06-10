
def read_matrix(n, m):
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    return matrix

def get_min_moves(matrix, d):
    n, m = len(matrix), len(matrix[0])
    min_moves = 0
    for i in range(n):
        for j in range(m):
            min_moves += abs(matrix[i][j] - d)
    return min_moves

def get_final_matrix(matrix, d):
    n, m = len(matrix), len(matrix[0])
    final_matrix = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            final_matrix[i][j] = d
    return final_matrix

def are_matrices_equal(matrix1, matrix2):
    n, m = len(matrix1), len(matrix1[0])
    for i in range(n):
        for j in range(m):
            if matrix1[i][j] != matrix2[i][j]:
                return False
    return True

def solve(n, m, d):
    matrix = read_matrix(n, m)
    min_moves = get_min_moves(matrix, d)
    final_matrix = get_final_matrix(matrix, d)
    if are_matrices_equal(matrix, final_matrix):
        return min_moves
    else:
        return -1

if __name__ == '__main__':
    n, m, d = map(int, input().split())
    print(solve(n, m, d))

