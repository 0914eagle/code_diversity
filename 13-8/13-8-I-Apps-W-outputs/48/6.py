
def read_input():
    n, m, d = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    return n, m, d, matrix

def find_min_moves(matrix, d):
    min_moves = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            min_moves += abs(matrix[i][j] - d)
    return min_moves

def solve(n, m, d, matrix):
    min_moves = find_min_moves(matrix, d)
    if min_moves == 0:
        return 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] % d != 0:
                return -1
    return min_moves

if __name__ == '__main__':
    n, m, d, matrix = read_input()
    print(solve(n, m, d, matrix))

