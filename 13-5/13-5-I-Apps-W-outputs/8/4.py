
def read_matrix(N, M):
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input().split())))
    return matrix

def get_sum(matrix, i, j):
    if i > len(matrix) or j > len(matrix[0]):
        return -1
    return matrix[i - 1][j - 1]

def get_max_sum(matrix, pairs):
    max_sum = -1
    for pair in pairs:
        sum1 = get_sum(matrix, pair[0], pair[1])
        sum2 = get_sum(matrix, pair[1], pair[0])
        max_sum = max(max_sum, max(sum1, sum2))
    return max_sum

def main():
    N, M = map(int, input().split())
    matrix = read_matrix(N, M)
    L = int(input())
    pairs = []
    for i in range(L):
        pairs.append(list(map(int, input().split())))
    print(get_max_sum(matrix, pairs))

if __name__ == '__main__':
    main()

