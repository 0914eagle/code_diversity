
def read_matrix(N, M):
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input().split())))
    return matrix

def get_sum(matrix, row, col):
    sum = 0
    for i in range(len(matrix)):
        if col < len(matrix[i]):
            sum += matrix[i][col]
        if row < len(matrix):
            sum += matrix[row][i]
    return sum

def solve(matrix, L):
    max_sum = -1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            sum1 = get_sum(matrix, i, j)
            sum2 = get_sum(matrix, j, i)
            max_sum = max(max_sum, max(sum1, sum2))
    return max_sum

def main():
    N, M = map(int, input().split())
    matrix = read_matrix(N, M)
    L = int(input())
    print(solve(matrix, L))

if __name__ == '__main__':
    main()

