
def get_matrix_sum(matrix, row, col):
    if row < len(matrix) and col < len(matrix[0]):
        return matrix[row][col]
    return 0

def get_matrix_sum_2(matrix, row, col):
    if col < len(matrix) and row < len(matrix[0]):
        return matrix[col][row]
    return 0

def get_max_sum(matrix, pairs):
    sum1 = 0
    sum2 = 0
    for pair in pairs:
        sum1 += get_matrix_sum(matrix, pair[0], pair[1])
        sum2 += get_matrix_sum_2(matrix, pair[0], pair[1])
    return max(sum1, sum2)

if __name__ == '__main__':
    matrix_size = input().split()
    matrix = []
    for _ in range(int(matrix_size[0])):
        matrix.append(list(map(int, input().split())))
    pairs_count = int(input())
    pairs = []
    for _ in range(pairs_count):
        pairs.append(list(map(int, input().split())))
    print(get_max_sum(matrix, pairs))

