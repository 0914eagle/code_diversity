
def get_matrix_sum(matrix, row, col):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == row or j == col:
                sum += matrix[i][j]
    return sum

def get_max_sum(matrix, pairs):
    max_sum = -1
    for pair in pairs:
        row, col = pair
        sum = get_matrix_sum(matrix, row, col)
        if sum > max_sum:
            max_sum = sum
    return max_sum

def main():
    matrix_size = input().split()
    N = int(matrix_size[0])
    M = int(matrix_size[1])
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

