
def get_matrix_sum(matrix, row, col):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == row or j == col:
                sum += matrix[i][j]
    return sum

def get_max_sum(matrix, pairs):
    max_sum = 0
    for pair in pairs:
        row = pair[0]
        col = pair[1]
        sum1 = get_matrix_sum(matrix, row, col)
        sum2 = get_matrix_sum(matrix, col, row)
        max_sum = max(max_sum, max(sum1, sum2))
    return max_sum

def main():
    N, M = map(int, input().split())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input().split())))
    L = int(input())
    pairs = []
    for i in range(L):
        pairs.append(list(map(int, input().split())))
    print(get_max_sum(matrix, pairs))

if __name__ == '__main__':
    main()

