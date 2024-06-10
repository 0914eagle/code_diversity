
def read_matrix(n, m):
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    return matrix

def find_min_moves(matrix, d):
    min_moves = 0
    while True:
        min_value = min(min(row) for row in matrix)
        max_value = max(max(row) for row in matrix)
        if min_value == max_value:
            break
        for row in matrix:
            for i in range(len(row)):
                if row[i] != min_value:
                    row[i] += d if row[i] > min_value else -d
        min_moves += 1
    return min_moves

def main():
    n, m, d = map(int, input().split())
    matrix = read_matrix(n, m)
    print(find_min_moves(matrix, d))

if __name__ == '__main__':
    main()

