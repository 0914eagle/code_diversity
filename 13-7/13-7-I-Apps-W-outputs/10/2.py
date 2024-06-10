
def get_input():
    n = int(input())
    vertices = list(map(int, input().split()))
    matrix = []
    for i in range(n):
        matrix.append(list(input()))
    return n, vertices, matrix

def get_color(matrix, i, j):
    if i == j:
        return '*'
    return matrix[i - 1][j - 1]

def get_connected_vertices(matrix, i, j):
    color = get_color(matrix, i, j)
    connected_vertices = []
    for k in range(len(matrix)):
        if get_color(matrix, i, k) == color and k != j:
            connected_vertices.append(k)
    return connected_vertices

def get_optimal_moves(n, vertices, matrix):
    moves = []
    for i in range(n):
        for j in range(n):
            if i != j and get_color(matrix, i, j) == get_color(matrix, vertices[0], vertices[1]) and get_color(matrix, vertices[0], vertices[1]) == get_color(matrix, vertices[1], vertices[2]):
                moves.append((i, j))
    return moves

def get_next_vertices(vertices, move):
    return [vertices[move[0]]] + [vertices[move[1]]] + [vertices[move[0]]]

def get_next_matrix(matrix, move):
    next_matrix = []
    for i in range(len(matrix)):
        next_matrix.append(matrix[i][:])
    next_matrix[move[0] - 1][move[1] - 1] = '*'
    next_matrix[move[1] - 1][move[0] - 1] = '*'
    return next_matrix

def solve(n, vertices, matrix):
    optimal_moves = get_optimal_moves(n, vertices, matrix)
    if not optimal_moves:
        return -1
    for move in optimal_moves:
        next_vertices = get_next_vertices(vertices, move)
        next_matrix = get_next_matrix(matrix, move)
        if next_vertices == [1, 2, 3]:
            return 1, move
        else:
            result = solve(n, next_vertices, next_matrix)
            if result != -1:
                return result + 1, move
    return -1

if __name__ == '__main__':
    n, vertices, matrix = get_input()
    result = solve(n, vertices, matrix)
    if result == -1:
        print(-1)
    else:
        print(result[0])
        print(result[1][0], result[1][1])

