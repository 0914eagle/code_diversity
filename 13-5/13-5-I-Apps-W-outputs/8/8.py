
def get_sum(matrix, row, col):
    if row < len(matrix) and col < len(matrix[0]):
        return matrix[row][col]
    else:
        return -1

def get_max_sum(matrix, pairs):
    max_sum = -1
    for pair in pairs:
        sum1 = get_sum(matrix, pair[0], pair[1])
        sum2 = get_sum(matrix, pair[1], pair[0])
        max_sum = max(max_sum, max(sum1, sum2))
    return max_sum

def main():
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    l = int(input())
    pairs = []
    for i in range(l):
        pairs.append(list(map(int, input().split())))
    print(get_max_sum(matrix, pairs))

if __name__ == '__main__':
    main()

