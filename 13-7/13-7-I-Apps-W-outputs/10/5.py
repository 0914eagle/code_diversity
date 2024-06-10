
def read_input():
    n = int(input())
    stones = list(map(int, input().split()))
    matrix = []
    for _ in range(n):
        matrix.append(list(input()))
    return n, stones, matrix

def get_moves(n, stones, matrix):
    moves = []
    for i in range(n):
        for j in range(i+1, n):
            if matrix[i][j] == matrix[stones[0]-1][stones[1]-1] and matrix[i][j] == matrix[stones[1]-1][stones[2]-1]:
                moves.append((i+1, j+1))
    return moves

def solve(n, stones, matrix):
    moves = get_moves(n, stones, matrix)
    if not moves:
        return -1
    return len(moves), moves

def main():
    n, stones, matrix = read_input()
    print(solve(n, stones, matrix))

if __name__ == '__main__':
    main()

