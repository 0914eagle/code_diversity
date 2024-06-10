
def get_input():
    n = int(input())
    vertices = [int(x) for x in input().split()]
    matrix = []
    for i in range(n):
        matrix.append(input())
    return n, vertices, matrix

def get_diagonal_color(matrix, i, j):
    if i == j:
        return '*'
    return matrix[i-1][j-1]

def get_neighbors(matrix, i, j):
    neighbors = []
    for k in range(1, len(matrix)+1):
        if k != i and k != j:
            diagonal_color = get_diagonal_color(matrix, i, k)
            if diagonal_color == get_diagonal_color(matrix, j, k):
                neighbors.append(k)
    return neighbors

def get_moves(matrix, vertices):
    moves = []
    for i in range(len(vertices)):
        for j in range(i+1, len(vertices)):
            if get_diagonal_color(matrix, vertices[i], vertices[j]) == get_diagonal_color(matrix, vertices[j], vertices[i]):
                moves.append((vertices[i], vertices[j]))
    return moves

def solve(n, vertices, matrix):
    moves = get_moves(matrix, vertices)
    if not moves:
        return -1
    return 1

if __name__ == '__main__':
    n, vertices, matrix = get_input()
    print(solve(n, vertices, matrix))

